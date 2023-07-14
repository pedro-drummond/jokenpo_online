import pygame
from pygame.locals import *
import sys
from time import sleep

# Inicialização do Pygame
pygame.init()

# Configurações da janela
HEIGHT = 800
WIDTH = 800

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0 , 0)

jokenpo = True
menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
