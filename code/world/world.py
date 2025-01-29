import pygame as pg
import numpy as np
from constants import colors
from perlin_noise import PerlinNoise

WORLD_SIZE = 50
TILE_SIZE = 64

class World:
    def __init__(self):
        self.noise = PerlinNoise(octaves=5, seed=np.random.randint(1000))
        self.tiles = self.generate_map()

    def generate_map(self):
        '''Tworzy mapę bazując na szumie Perlina'''
        tiles = []

        for y in range(WORLD_SIZE):
            row = []

            for x in range(WORLD_SIZE):
                value = self.noise([x / WORLD_SIZE, y / WORLD_SIZE])
                
                if value > 0.3:
                    row.append('grass')
                else:
                    row.append('water')

            tiles.append(row)

        return tiles
    

    def draw(self, screen):
        '''Rysuje mapę świata na ekranie'''
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                if tile == 'grass':
                    color = colors.GREEN
                else:
                    color = colors.BLUE

                pg.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

