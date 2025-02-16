import pygame
import sys
from settings import *

def check_events(pacman):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pacman.moving_right = True
            elif event.key == pygame.K_LEFT:
                pacman.moving_left = True
            elif event.key == pygame.K_UP:
                pacman.moving_up = True
            elif event.key == pygame.K_DOWN:
                pacman.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                pacman.moving_right = False
            elif event.key == pygame.K_LEFT:
                pacman.moving_left = False
            elif event.key == pygame.K_UP:
                pacman.moving_up = False
            elif event.key == pygame.K_DOWN:
                pacman.moving_down = False

def update_screen(screen, pacman):
    """Update images on the screen and flip to the new screen."""
    screen.fill((0, 0, 0))
    pacman.blitme()
    pygame.display.flip()
    pygame.display.flip()