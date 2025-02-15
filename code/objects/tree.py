import pygame as pg
from items.wood import Wood
from random import randint
from constants.tiles import TILE_SIZE
from utils.textures_utils import get_texture

class Tree(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = get_texture(name='tree', size=(64, 64))
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE, y * TILE_SIZE))
        self.mask = pg.mask.from_surface(self.image)
        
        self.type = 'tree'
        self.walkable = False
        self.interactable = True
        self.health = 3
        self.drop = Wood(randint(1, 3))
        

    def interact(self):
        if self.health > 0:
            self.health -= 1

            if self.health <= 0:
                return 'destroy', self.drop
            
        return None, None


    def draw(self, screen, offset_x, offset_y):
        x = self.rect.x - offset_x
        y = self.rect.y - offset_y

        screen.blit(self.image, (x, y))
