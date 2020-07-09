import pygame

gravity = 0.07


class QueenSprite:

    def __init__(self, img, target_posn):
        """ Create and initialize a queen for this
            target position on the board
        """
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)  # Start ball at top of its column
        self.y_velocity = 0  # with zero initial velocity

    def update(self):
        self.y_velocity += gravity               # Do nothing for the moment.
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity
        (target_x, target_y) = self.target_posn
        dist_to_go = target_y - new_y_pos

        if dist_to_go < 0:
            self.y_velocity = -0.65 * self.y_velocity
            new_y_pos = target_y +dist_to_go

        self.posn = (x, new_y_pos)

    def draw(self, target_surfacse):
        target_surfacse.blit(self.image, self.posn)

    def contains_point(self, pt):
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return (x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)

    def handle_click(self):
        self.y_velocity += -4 # kick it up


class DukeSprite:
    def __init__(self, img, target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.anim_frame_count > 0:
            self. anim_frame_count = (self.anim_frame_count + 1) % 60
            self.curr_patch_num = self.anim_frame_count // 6
        return

    def handle_click(self):
        if self.anim_frame_count == 0:
            self.anim_frame_count = 5
        return

    def contains_point(self, pt):
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return (x >= my_x and x < my_x + 50 and y >= my_y and y < my_y + my_height)

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0, 50, self.image.get_height())
        target_surface.blit(self.image, self.posn, patch_rect)
        # ask FOR HELP>>>

def draw_board_2(the_board):
    """ Draw a chess board with queens, from the_board. """

    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]    # Set up colors [red, black]

    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    duke_sprite_sheet = pygame.image.load("duke_spritesheet.png")

    duke1 = DukeSprite(duke_sprite_sheet, (sq_sz * 2, 0))
    duke2 = DukeSprite(duke_sprite_sheet, (sq_sz * 5, sq_sz))

    ball = pygame.image.load("beachball_2.png")
    ball = pygame.transform.scale(ball, (30, 30))

    my_clock = pygame.time.Clock()


    ball_offset = (sq_sz - ball.get_width()) // 2

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    all_sprites = []  # Keep a list of all sprites in the game

    # Create a sprite object for each queen, and populate our list.
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball, (col*sq_sz+ball_offset, row*sq_sz+ball_offset))
        all_sprites.append(a_queen)
        all_sprites.append(duke1)
        all_sprites.append(duke2)

    while True:
        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 27:
                break
            if key == ord("r"):
                colors[0] = (255, 0, 0)
            elif key == ord("g"):
                colors[0] = (0, 255, 0)
            elif key == ord("b"):
                colors[0] = (0, 0, 255)

        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict["pos"]
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
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

        my_clock.tick(60)

        pygame.display.flip()
    pygame.quit()



if __name__ == "__main__":
    draw_board_2([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
    draw_board_2([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board_2([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    draw_board_2([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
