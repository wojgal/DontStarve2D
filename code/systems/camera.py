import pygame as pg
from constants.tiles import TILE_SIZE
from constants.world import WORLD_SIZE
from constants.tiles import VISIBLE_TILES_X, VISIBLE_TILES_Y

class Camera:
    def __init__(self, player, display_width, display_height):
        self.player = player
        self.width = display_width
        self.height = display_height

    def get_offset(self):
        offset_x = self.player.rect.x - self.width // 2 + TILE_SIZE // 2
        offset_y = self.player.rect.y - self.height // 2 + TILE_SIZE // 2

        return offset_x, offset_y
    
    
    def get_tiles_offset(self):
        offset_x, offset_y = self.get_offset()

        return offset_x // TILE_SIZE, offset_y // TILE_SIZE
    

    def get_tiles_range(self):
        tile_offset_x, tile_offset_y = self.get_tiles_offset()

        start_tile_x = max(0, tile_offset_x)
        start_tile_y = max(0, tile_offset_y)

        end_tile_x = min(WORLD_SIZE, tile_offset_x + VISIBLE_TILES_X)
        end_tile_y = min(WORLD_SIZE, tile_offset_y + VISIBLE_TILES_Y)

        return start_tile_x, start_tile_y, end_tile_x, end_tile_y
    

