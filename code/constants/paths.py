TEXTURE_PATHS = {
    'grass': 'assets/textures/grass.png',
    'grass_leaves1': 'assets/textures/grass_leaves1.png',
    'grass_leaves2': 'assets/textures/grass_leaves2.png',
    'grass_leaves3': 'assets/textures/grass_leaves3.png',
    'water': 'assets/textures/water.png',
    'tree': 'assets/textures/tree.png',
    'inventory': 'assets/textures/inventory.png',
    'wood': 'assets/textures/wood.png'
}
SPRITE_SHEET_PATHS = {
    'player': {
        'path': 'assets/sprites/player.png',
        # 'name': (frame_width, frame_height, number_of_frames, row, flip_vertical)
        'idle_down': (32, 32, 6, 0, False),
        'idle_right': (32, 32, 6, 1, False),
        'idle_up': (32, 32, 6, 2, False),
        'idle_left': (32, 32, 6, 1, True),

        'move_down': (32, 32, 6, 3, False),
        'move_right': (32, 32, 6, 4, False),
        'move_up': (32, 32, 6, 5, False),
        'move_left': (32, 32, 6, 4, True),

        'attack_down': (32, 32, 4, 6, False),
        'attack_right': (32, 32, 4, 7, False),
        'attack_up': (32, 32, 4, 8, False),
        'attack_left': (32, 32, 4, 7, True)
    }
}

FONT_PATHS = {
    'main': 'assets/fonts/upheavtt.ttf',
}

MUSIC_PATHS = {
    'music': 'assets/music/music1.ogg',
}

SFX_PATHS = {
    'attack_sword': 'assets/sfx/attack_sword.wav',
    'walk': 'assets/sfx/walk.wav',
}


