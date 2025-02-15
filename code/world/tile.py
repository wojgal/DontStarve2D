import pygame as pg
from constants.tiles import TILE_SIZE, TILE_TYPES

class Tile:
    def __init__(self, type: str, x: int, y: int):
        '''Tworzy kafelek o określonmy typie'''
        self.type = type
        self.x = x
        self.y = y

        self.size = TILE_SIZE

        self.walkable = TILE_TYPES[self.type]['walkable']
        self.texture = TILE_TYPES[self.type]['texture']

    def draw(self, screen, offset_x, offset_y):
        '''Rysuje kafelek na ekranie'''
        x = self.x * self.size - offset_x
        y = self.y * self.size - offset_y
        screen.blit(self.texture, (x, y))
