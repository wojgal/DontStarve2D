import pygame as pg
import numpy as np
from constants import colors
from world.tilemap import TileMap

WORLD_SIZE = 30
TILE_SIZE = 64

class World:
    def __init__(self):
        self.map = TileMap(WORLD_SIZE)
    

    def draw(self, screen):
        self.map.draw(screen)

    def get_map(self):
        return self.map


