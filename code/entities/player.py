import pygame as pg
from systems.inventory import Inventory
from constants.tiles import TILE_SIZE
from constants.controls import INPUT_MAPPING
from constants.player import PLAYER_HEALTH, PLAYER_SPEED
from utils.animation import Animation
from utils.textures_utils import get_sprites

from constants import colors

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, world):
        super().__init__()

        self.world = world
        self.inventory = Inventory()

        self.speed = PLAYER_SPEED
        self.health = PLAYER_HEALTH
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

        self.image = self.animations[self.state][self.direction].get_current_frame()
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE, y * TILE_SIZE))


    def check_move_on_tiles(self, tiles_cords):
        for x, y in tiles_cords:
            tile = self.world.get_tile(x, y)

            if tile is None:
                return False
            
            if tile.walkable is False:
                return False
            
        return True


    def check_no_collision_with_objects(self, tiles_cords):
        for x, y in tiles_cords:
            object = self.world.get_object_at(x, y)

            if object is None:
                continue

            if object.walkable is False:
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

        if self.check_move_on_tiles(tiles_cords) is False:
            return False
        
        if self.check_no_collision_with_objects(tiles_cords) is False:
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
    

    def get_facing_tile_cords(self):
        tile_x, tile_y = self.rect.center
        tile_x, tile_y = tile_x // TILE_SIZE, tile_y // TILE_SIZE

        if self.direction == 'up':
            tile_y -= 1
        
        elif self.direction == 'down':
            tile_y += 1

        elif self.direction == 'left':
            tile_x -= 1
        
        elif self.direction == 'right':
            tile_x += 1

        return tile_x, tile_y
    

    def get_facing_object(self):
        tile_x, tile_y = self.get_facing_tile_cords()

        return self.world.get_object_at(tile_x, tile_y)


    def handle_attack(self, keys):
        '''Obsluguje atak gracza'''
        if any(keys[key] for key in INPUT_MAPPING['attack']):
            self.action_timer = self.animations['attack'][self.direction].get_timer()

            object = self.get_facing_object()

            if object and hasattr(object, 'interact'):
                result, drop = object.interact()

                if result == 'destroy':
                    self.world.remove_object(object)
                    self.inventory.add_item(drop)

            return 'attack'
        
        return 'idle'

        
    def handle_input(self, keys):
        # Dzięki temu mamy pewność, że nie jest wykonywana żadna akcja w dalszej części kodu
        if self.action_timer > 0:
            return 
        
        new_state = self.handle_attack(keys)

        if new_state == 'idle':
            new_state = self.handle_movement(keys)

        self.state = new_state


    def handle_events(self, events):
        keys = pg.key.get_pressed()

        for event in events:
            if event.type == pg.KEYDOWN:

                if event.key in INPUT_MAPPING['inventory']:
                    self.inventory.toggle_open()

        if not self.inventory.is_open:
            self.handle_input(keys)


    def update(self, dt):
        if self.action_timer > 0:
            self.action_timer -= dt

            if self.action_timer <= 0:
                self.action_timer = 0
                self.animations[self.state][self.direction].reset_animation()
                self.state = 'idle'
                self.animations[self.state][self.direction].reset_animation()
                
        self.animations[self.state][self.direction].update(dt)
        self.image = self.animations[self.state][self.direction].get_current_frame()
    

    def draw_facing_tile(self, screen):
        tile_x, tile_y = self.get_facing_tile_cords()

        highlight_surface = pg.Surface((TILE_SIZE, TILE_SIZE), pg.SRCALPHA)
        highlight_surface.fill((255, 255, 255, 25))

        screen.blit(highlight_surface, (tile_x * TILE_SIZE, tile_y * TILE_SIZE))


    def draw(self, screen):
        #pg.draw.rect(screen, colors.RED, self.rect)
        self.draw_facing_tile(screen)
        screen.blit(self.image, self.rect)
        self.inventory.draw(screen)



