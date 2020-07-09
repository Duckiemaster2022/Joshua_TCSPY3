import pygame


def draw_board(the_board):
    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]

    ball = pygame.image.load("th.jpg")

    n = len(the_board)
    surface_sz = 480
    sq_sz = surface_sz // n
    surface_sz = n * sq_sz
    ball_offset = (sq_sz - ball.get_width()) // 2

    surface = pygame.display.set_mode((surface_sz, surface_sz))
    pygame.transform.scale(ball, (300, 300))


    while True:

        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        for row in range(n):
            c_indx = row % 2
            for col in range(n):
                the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                c_indx = (c_indx + 1) % 2

        for (col, row) in enumerate(the_board):
            surface.blit(ball, (col * sq_sz + ball_offset, row * sq_sz + ball_offset))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    draw_board([0, 5, 3, 1, 6, 4, 2])
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])
    draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
