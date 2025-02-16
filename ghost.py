import pygame
import random
from settings import *

class Ghost:
    def __init__(self, screen, color, personality):
        self.screen = screen
        self.normal_color = color
        self.vulnerable_color = (0, 0, 255)  # Blue when vulnerable
        self.current_color = color
        self.personality = personality
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.screen_rect = screen.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.vulnerable = False
        self.speed = GHOST_SPEED
        self.direction = random.choice(['right', 'left', 'up', 'down'])
        
        self.behaviors = {
            'chaser': self.chase_pacman,
            'ambusher': self.ambush_pacman,
            'random': self.move_random,
            'patrol': self.patrol_area
        }

    def chase_pacman(self):
        # Basic movement for now
        self.move_random()

    def ambush_pacman(self):
        # Basic movement for now
        self.move_random()

    def move_random(self):
        if random.random() < 0.02:  # 2% chance to change direction
            self.direction = random.choice(['right', 'left', 'up', 'down'])

    def patrol_area(self):
        # Basic movement for now
        self.move_random()

    def update(self):
        self.behaviors[self.personality]()
        
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
            
        # Keep ghost in bounds
        self.rect.clamp_ip(self.screen_rect)
        
    def draw(self):
        pygame.draw.circle(self.screen, self.current_color, self.rect.center, 15)
