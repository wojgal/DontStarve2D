import pygame as pg
from constants import colors
from utils.textures_utils import get_texture

class Tree:
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 64, 64)
        self.type = 'tree'
        self.walkable = False
        self.interactable = True
        self.health = 3
        self.texture = get_texture(name='tree', size=(128, 128))

    def interact(self):
        if self.health > 0:
            self.health -= 1

            if self.health <= 0:
                return 'destroy'
            
        return None

    def draw(self, screen):
        if self.texture:
            screen.blit(self.texture, self.rect)

        else:
            pg.draw.rect(screen, colors.GREEN, self.rect)

