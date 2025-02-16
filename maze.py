import pygame

class Maze:
    def __init__(self, screen):
        self.screen = screen
        self.walls = []
        self.cell_size = 30
        self.layout = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "W............WW............W",
            "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
            "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
            "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
            "W..........................W",
            "W.WWWW.WW.WWWWWWWW.WW.WWWW.W",
            "W.WWWW.WW.WWWWWWWW.WW.WWWW.W",
            "W......WW....WW....WW......W",
            "WWWWWW.WWWWW WW WWWWW.WWWWWW",
            "     W.WWWWW WW WWWWW.W     ",
            "     W.WW          WW.W     ",
            "     W.WW WWW--WWW WW.W     ",
            "WWWWWW.WW W      W WW.WWWWWW",
            "      .   W      W   .      ",
            "WWWWWW.WW W      W WW.WWWWWW",
            "     W.WW WWWWWWWW WW.W     ",
            "     W.WW          WW.W     ",
            "     W.WW WWWWWWWW WW.W     ",
            "WWWWWW.WW WWWWWWWW WW.WWWWWW",
            "W............WW............W",
            "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
            "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
            "W...WW................WW...W",
            "WWW.WW.WW.WWWWWWWW.WW.WW.WWW",
            "WWW.WW.WW.WWWWWWWW.WW.WW.WWW",
            "W......WW....WW....WW......W",
            "W.WWWWWWWWWW.WW.WWWWWWWWWW.W",
            "W.WWWWWWWWWW.WW.WWWWWWWWWW.W",
            "W..........................W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW"
        ]
        self.create_walls()

    def create_walls(self):
        for row_index, row in enumerate(self.layout):
            for col_index, cell in enumerate(row):
                if cell == "W":
                    x = col_index * self.cell_size
                    y = row_index * self.cell_size
                    wall = pygame.Rect(x, y, self.cell_size, self.cell_size)
                    self.walls.append(wall)

    def draw(self):
        for wall in self.walls:
            pygame.draw.rect(self.screen, (0, 0, 255), wall)  # Blue walls

    def check_collision(self, rect):
        return any(wall.colliderect(rect) for wall in self.walls)
