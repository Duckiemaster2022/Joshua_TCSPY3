import pygame


class QueenSprite:

    def __init__(self, img, target_posn):
        """ Create and initialize a queen for this
            target position on the board
        """
        self.image = img
        self.target_posn = target_posn
        self.posn = target_posn

    def update(self):
        return                # Do nothing for the moment.

    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)


def draw_board_2(the_board):
    """ Draw a chess board with queens, from the_board. """

    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]    # Set up colors [red, black]

    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    ball = pygame.image.load("beachball_2.png")
    ball = pygame.transform.scale(ball, (30, 30))

    ball_offset = (sq_sz - ball.get_width()) // 2

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    all_sprites = []  # Keep a list of all sprites in the game

    # Create a sprite object for each queen, and populate our list.
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball, (col*sq_sz+ball_offset, row*sq_sz+ball_offset))
        all_sprites.append(a_queen)

    while True:
        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # Ask every sprite to update itself.
        for sprite in all_sprites:
            sprite.update()

        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Change starting color on each row
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # now flip the color index for the next square
                c_indx = (c_indx + 1) % 2
                
        # Ask every sprite to draw itself.
        for sprite in all_sprites:
            sprite.draw(surface)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    draw_board_2([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
    draw_board_2([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board_2([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    draw_board_2([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
