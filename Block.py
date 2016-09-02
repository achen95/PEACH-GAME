from SpriteSheet import *
import pygame


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32

    def renderSky(self, screen):
        pygame.draw.rect(screen, (110, 193, 248),
                         (self.x, self.y, self.width, self.height))

    def renderDirt(self, screen):
        pygame.draw.rect(screen, (139, 69, 19),
                         (self.x, self.y, self.width, self.height))

    def renderGrass(self, screen):
        pygame.draw.rect(screen, (0, 155, 0),
                         (self.x, self.y, self.width, self.height))

    def renderBuilding(self, screen):
        buildingRect = pygame.draw.rect(screen, (255, 0, 0),
                                        (self.x, self.y, self.width, self.height))
        return buildingRect



