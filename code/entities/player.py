import pygame as pg
from constants import colors
from constants.tiles import TILE_SIZE
from constants.controls import INPUT_MAPPING
from utils.animation import Animation
from utils.textures_utils import get_sprites

class Player:
    def __init__(self, x, y, width, height, world):
        self.rect = pg.Rect(x, y, width, height)
        self.world = world

        self.speed = 4
        self.health = 10
        self.action_timer = 0
        self.state = 'idle'
        self.direction = 'right'

        self.animations = {
            'idle': {
                'down': Animation(get_sprites('player', 'idle_down'), frame_duration=175),
                'right': Animation(get_sprites('player', 'idle_right'), frame_duration=175),
                'up': Animation(get_sprites('player', 'idle_up'), frame_duration=175),
                'left': Animation(get_sprites('player', 'idle_left'), frame_duration=175)             
            },
            
            'move': {
                'down': Animation(get_sprites('player', 'move_down'), frame_duration=125),
                'right': Animation(get_sprites('player', 'move_right'), frame_duration=125),
                'up': Animation(get_sprites('player', 'move_up'), frame_duration=125),
                'left': Animation(get_sprites('player', 'move_left'), frame_duration=125)
            },

            'attack': {
                'down': Animation(get_sprites('player', 'attack_down'), frame_duration=125),
                'right': Animation(get_sprites('player', 'attack_right'), frame_duration=125),
                'up': Animation(get_sprites('player', 'attack_up'), frame_duration=125),
                'left': Animation(get_sprites('player', 'attack_left'), frame_duration=125),
            }
        }

    def check_move_on_tiles(self, tiles_cords):
        for x, y in tiles_cords:
            tile = self.world.get_tile(x, y)

            if tile is None or not tile.walkable:
                return False
            
        return True


    def check_no_collision_with_objects(self, tiles_cords):
        for x, y in tiles_cords:
            object = self.world.get_object_at(x * TILE_SIZE, y * TILE_SIZE)

            if object is not None and not object.walkable:
                return False
            
        return True


    def can_move(self, new_x, new_y):
        '''Sprawdza, czy gracz moze wejsc na dane kafelki'''
        # wszystkie mozliwe kafelki na ktorych moze znalezc sie gracz
        tiles_cords = [
            [new_x // TILE_SIZE, new_y // TILE_SIZE],
            [(new_x + self.rect.width - 1) // TILE_SIZE, new_y // TILE_SIZE],
            [new_x // TILE_SIZE, (new_y + self.rect.height - 1) // TILE_SIZE],
            [(new_x + self.rect.width - 1) // TILE_SIZE, (new_y + self.rect.height - 1) // TILE_SIZE]
        ]

        if not self.check_move_on_tiles(tiles_cords):
            return False
        
        if not self.check_no_collision_with_objects(tiles_cords):
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
            self.direction = 'up'
            dy -= 1

        if any(keys[key] for key in INPUT_MAPPING['move_down']):
            self.direction = 'down'
            dy += 1

        if any(keys[key] for key in INPUT_MAPPING['move_left']):
            self.direction = 'left'
            dx -= 1

        if any(keys[key] for key in INPUT_MAPPING['move_right']):
            self.direction = 'right'
            dx += 1

        if dx or dy:
            self.move(dx, dy)
            return 'move'
        
        return 'idle'


    def handle_attack(self, keys):
        '''Obsluguje atak gracza'''
        if any(keys[key] for key in INPUT_MAPPING['attack']):
            self.action_timer = self.animations['attack'][self.direction].get_timer()
            return 'attack'
        
        return 'idle'

        
    def handle_input(self, keys):
        # Dzięki temu mamy pewność, że nie jest wykonywana żadna akcja w dalszej części kodu
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
                self.animations[self.state][self.direction].reset_animation()
                self.state = 'idle'
                self.animations[self.state][self.direction].reset_animation()

        self.animations[self.state][self.direction].update(dt)
    

    def draw(self, screen):
        screen.blit(self.animations[self.state][self.direction].get_current_frame(), self.rect)
        #pg.draw.rect(screen, colors.RED, self.rect)

