import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

preto = (0,0,0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')
