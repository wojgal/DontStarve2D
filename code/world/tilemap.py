from world.tile import Tile
from perlin_noise import PerlinNoise
from numpy.random import randint

class TileMap:
    def __init__(self, world_size: int):
        self.world_size = world_size

        self.noise = PerlinNoise(octaves=4, seed=randint(1000))
        self.tiles = self.generate_map()


    def generate_map(self):
        '''Generowanie mapy bazujac na szumie Perlina'''
        tiles = []

        for y in range(self.world_size):
            row = []
            for x in range(self.world_size):
                perlin_value = self.noise([x / self.world_size, y / self.world_size])
                normalized_value = (perlin_value + 1) / 2
                
                if 0 <= normalized_value < 0.4:
                    tile = Tile(type='water', x=x, y=y)

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
        if not 0 <= x < self.world_size:
            return None
        
        # y jest poza zakresem
        if not 0 <= y < self.world_size:
            return None
        
        return self.tiles[y][x]