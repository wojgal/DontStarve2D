from utils.animation import Animation
from utils.textures_utils import get_sprites

PLAYER_SPEED = 4
PLAYER_HEALTH = 10

ANIMATIONS = {
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