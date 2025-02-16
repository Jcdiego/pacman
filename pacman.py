import pygame
import sys
from settings import *
from game_functions import check_events, update_screen
from pacman_sprite import Pacman
from pellet import Pellet
from ghost import Ghost

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 930))  # Adjusted for maze size
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        from maze import Maze
        self.maze = Maze(self.screen)
        self.pacman = Pacman(self.screen)
        self.pellets = self.create_pellets()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.ghosts = self.create_ghosts()   
        self.lives = 3
        self.level = 1
        self.score = 0
        self.power_pellets = self.create_power_pellets()
        self.fruits = []
        self.ghost_score = 200

    def create_ghosts(self):
        return [
            Ghost(self.screen, (255, 0, 0), 'chaser'),      # Red ghost - chases Pacman
            Ghost(self.screen, (0, 255, 255), 'ambusher'),  # Cyan ghost - tries to ambush
            Ghost(self.screen, (255, 182, 255), 'random'),  # Pink ghost - moves randomly
            Ghost(self.screen, (255, 182, 85), 'patrol')    # Orange ghost - patrols area
        ]


    def create_pellets(self):
        pellets = []
        for x in range(30, SCREEN_WIDTH, 60):
            for y in range(30, SCREEN_HEIGHT, 60):
                pellets.append(Pellet(self.screen, x, y))
        return pellets

    def run(self):
        while True:
            check_events(self.pacman)
            self.pacman.update(self.maze)
            for ghost in self.ghosts:
                ghost.update()

            self.screen.fill((0, 0, 0))
            self.maze.draw()
            for pellet in self.pellets:
                pellet.draw()
            self.pacman.blitme()
            for ghost in self.ghosts:
                ghost.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def create_power_pellets(self):
        from power_pellet import PowerPellet
        return [
            PowerPellet(self.screen, 30, 30),
            PowerPellet(self.screen, 870, 30),
            PowerPellet(self.screen, 30, 900),
            PowerPellet(self.screen, 870, 900)
        ]
        
        
    def spawn_fruit(self):
        import random
        try:
            from fruit import Fruit
        except ImportError:
            sys.path.append('/c:/Users/Acer/Downloads/games/pacman_game')
            from fruit import Fruit
        if random.random() < 0.005:  # 0.5% chance each frame
            fruit = Fruit(self.screen)
            self.fruits.append(fruit)

    def check_collisions(self):
        # Check power pellet collisions
        for pellet in self.power_pellets[:]:
            if self.pacman.rect.colliderect(pellet.rect):
                self.power_pellets.remove(pellet)
                self.make_ghosts_vulnerable()
                # Check ghost collisions
        for ghost in self.ghosts:
            if self.pacman.rect.colliderect(ghost.rect):
                if ghost.vulnerable:
                    self.score += self.ghost_score
                    self.ghost_score *= 2
                else:
                    self.lives -= 1
                    if self.lives <= 0:
                        self.game_over()
                    else:
                        self.reset_level()

        def draw_ui(self):
            # Draw score
            score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))
            
            # Draw lives
            for i in range(self.lives):
                pygame.draw.circle(self.screen, (255, 255, 0), (30 + i*30, 850), 10)
                
            # Draw level
            level_text = self.font.render(f'Level: {self.level}', True, (255, 255, 255))
            self.screen.blit(level_text, (750, 10))




if __name__ == '__main__':
    game = Game()
    game.run()
