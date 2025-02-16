import pygame
from settings import *

class Pacman:
    """A class to manage Pacman."""

    def __init__(self, screen):
        """Initialize Pacman and set its starting position."""
        self.screen = screen
        # Create a transparent surface for Pacman
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center

        # Start each new Pacman at the center of the screen
        self.rect.center = self.screen_rect.center

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self, maze):
        """Update Pacman's position based on movement flags and wall collisions."""
        # Store original position for collision checking
        original_x = self.rect.x
        original_y = self.rect.y

        if self.moving_right:
            self.rect.x += PACMAN_SPEED
        if self.moving_left:
            self.rect.x -= PACMAN_SPEED
        if self.moving_up:
            self.rect.y -= PACMAN_SPEED
        if self.moving_down:
            self.rect.y += PACMAN_SPEED

        # Check for wall collisions and revert position if needed
        if maze.check_collision(self.rect):
            self.rect.x = original_x
            self.rect.y = original_y

    def blitme(self):
        """Draw Pacman at its current location."""
        # Draw yellow circle
        pygame.draw.circle(self.screen, (255, 255, 0), self.rect.center, 15)
        # Draw mouth (triangle)
        points = [
            self.rect.center,
            (self.rect.centerx + 15, self.rect.centery - 10),
            (self.rect.centerx + 15, self.rect.centery + 10)
        ]
        pygame.draw.polygon(self.screen, (0, 0, 0), points)
