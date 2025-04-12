import pygame
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def def_font(size):
    return pygame.font.Font("assets/font.ttf", size)


