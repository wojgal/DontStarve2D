import pygame as pg
from constants import colors
from constants.tiles import TILE_SIZE
from constants.controls import INPUT_MAPPING
from utils.animation import Animation
from utils.textures_utils import get_sprites
from math import sqrt

class Player:
    def __init__(self, x, y, width, height, world):
        self.rect = pg.Rect(x, y, width, height)
        self.world = world

        self.speed = 4
        self.health = 100
        self.action_timer = 0
        self.state = 'idle'

        self.animations = {
            'walk': Animation(get_sprites(sheet_name='character', sprite_name='walk', size=(96, 96)), frame_duration=150),
            'idle': Animation(get_sprites(sheet_name='character', sprite_name='idle1', size=(96, 96)), frame_duration=1000),
            'dead': Animation(get_sprites(sheet_name='character', sprite_name='dead', size=(96, 96)), frame_duration=300),
            'attack': Animation(get_sprites(sheet_name='character', sprite_name='attack', size=(96, 96)), frame_duration=100)
        }



    def can_move(self, new_x, new_y):
        '''Sprawdza, czy gracz moze wejsc na dane kafelki'''
        map = self.world.get_map()

        # wszystkie mozliwe kafelki na ktorych moze znalezc sie gracz
        tiles_cords = [
            [new_x // TILE_SIZE, new_y // TILE_SIZE],
            [(new_x + self.rect.width - 1) // TILE_SIZE, new_y // TILE_SIZE],
            [new_x // TILE_SIZE, (new_y + self.rect.height - 1) // TILE_SIZE],
            [(new_x + self.rect.width - 1) // TILE_SIZE, (new_y + self.rect.height - 1) // TILE_SIZE]
        ]

        tiles_objects = []

        for x, y in tiles_cords:
            tiles_objects.append(map.get_tile(x, y))

        for tile in tiles_objects:
            if tile is None:
                return False
            
            if not tile.walkable:
                return False
            
        return True


    def move(self, dx, dy):
        '''Obsluguje ruch gracza'''
        new_x = self.rect.x + dx * self.speed
        new_y = self.rect.y + dy * self.speed

        # Sprawdzamy ruch w poziomie
        if self.can_move(new_x, self.rect.y):
            self.rect.x = new_x

        if self.can_move(self.rect.x, new_y):
            self.rect.y = new_y


    def handle_movement(self, keys):
        '''Obsluguje ruch gracza'''
        dx, dy = 0, 0

        if any(keys[key] for key in INPUT_MAPPING['move_up']):
            dy -= 1

        if any(keys[key] for key in INPUT_MAPPING['move_down']):
            dy += 1

        if any(keys[key] for key in INPUT_MAPPING['move_left']):
            dx -= 1

        if any(keys[key] for key in INPUT_MAPPING['move_right']):
            dx += 1

        if dx or dy:
            self.move(dx, dy)
            return 'walk'
        
        return 'idle'


    def handle_attack(self, keys):
        '''Obsluguje atak gracza'''
        if self.action_timer <= 0 and any(keys[key] for key in INPUT_MAPPING['attack']):
            self.action_timer = self.animations['attack'].get_timer()
            return 'attack'
        
        return 'idle'

        
    def handle_input(self, keys):
        if self.action_timer > 0:
            return 
        
        state = self.handle_attack(keys)

        if state == 'idle':
            state = self.handle_movement(keys)

        self.state = state


    def update(self, dt):
        if self.action_timer > 0:
            self.action_timer -= dt

        if self.action_timer <= 0:
            self.action_timer = 0
            self.state = 'idle'

        # for name, animation in self.animations.items():
        #     if name == self.state:
        #         continue

        #     animation.reset_animation()

        self.animations[self.state].update(dt)
    

    def draw(self, screen):
        screen.blit(self.animations[self.state].get_current_frame(), self.rect)
        #pg.draw.rect(screen, colors.RED, self.rect)

