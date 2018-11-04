import pygame
pygame.init()

s = 1
majakuubik1 = pygame.image.load("1.png")
aken = pygame.display.set_mode((800, 600))
if s == 1:
    aken.blit(majakuubik1, (400,500))