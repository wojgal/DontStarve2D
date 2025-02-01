from world.tile import Tile
from perlin_noise import PerlinNoise
from numpy.random import randint

class TileMap:
    def __init__(self, size: int, noise):
        self.size = size
        self.noise = noise
        self.tiles = self.generate_map()


    def generate_map(self):
        '''Generowanie mapy bazujac na szumie Perlina'''
        tiles = []

        for y in range(self.size):
            row = []
            for x in range(self.size):
                perlin_value = self.noise([x / self.size, y / self.size])
                normalized_value = (perlin_value + 1) / 2
                
                # Woda
                if 0 <= normalized_value < 0.4:
                    tile = Tile(type='water', x=x, y=y)

                # Trawa
                elif 0.4 <= normalized_value <=1:
                    tile = Tile(type='grass', x=x, y=y)

                row.append(tile)

            tiles.append(row)

        return tiles


    def draw(self, screen):
        '''Rysuje wszystkie kafelki na ekranie'''
        for row in self.tiles:
            for tile in row:
                tile.draw(screen)


    def get_tile(self, x: int, y: int):
        '''Zwraca obiekt kafelka na danej pozycji'''
        # x jest poza zakresem
        if not 0 <= x < self.size:
            return None
        
        # y jest poza zakresem
        if not 0 <= y < self.size:
            return None
        
        return self.tiles[y][x]
    