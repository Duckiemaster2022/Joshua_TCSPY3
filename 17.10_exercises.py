import pygame
import random


rng = random.Random()

class Cards:

    def __init__(self, image, display_position):
        self.img = image
        self.posn = display_position

    def update(self):
        self.posn.x += 40

    def draw(self, target_surface, card_num):
        print(self, target_surface, card_num)
        if card_num / 2 >= 2:
            patch_rect = (card_num * 50, -50, 50, 50)

        target_surface.blit(self.image, self.posn, patch_rect)
        return


def display_cards():
    pygame.init()
    surface_sz = 500
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    cards = pygame.image.load("playcards.png")
    card_nums = list(range(1, 53))

    rng.shuffle(card_nums)
    card_nums = card_nums[:5]

    Cards.__init__(cards, (100, 100))
    while True:
        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.MOUSEBUTTONDOWN:
            for i in card_nums:
                Cards.draw(surface, i)

display_cards()
