from world.tile import Tile
from numpy.random import randint

class TileMap:
    def __init__(self, size, noise):
        self.size = size
        self.noise = noise
        self.camera = None
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
        start_tile_x, start_tile_y, end_tile_x, end_tile_y = self.camera.get_tiles_range()
        tile_offset_x, tile_offset_y = self.camera.get_offset()

        for y in range(start_tile_y, end_tile_y):
            for x in range(start_tile_x, end_tile_x):
                tile = self.tiles[y][x]
                tile.draw(screen, tile_offset_x, tile_offset_y)


    def get_tile(self, x: int, y: int):
        '''Zwraca obiekt kafelka na danej pozycji'''
        # x jest poza zakresem
        if 0 <= x < self.size is False:
            return None
        
        # y jest poza zakresem
        if 0 <= y < self.size is False:
            return None
        print(x,y)
        return self.tiles[y][x]
    