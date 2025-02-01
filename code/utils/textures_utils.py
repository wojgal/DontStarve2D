import pygame as pg
from constants.paths import TEXTURE_PATHS, SPRITE_SHEET_PATHS

texture_cache = {}

pg.display.init()
pg.display.set_mode(size=(1, 1), flags=pg.HIDDEN)


def load_texture_file(path: str):
    texture = pg.image.load(path).convert_alpha()

    return texture


def get_texture(name: str, size: tuple=(64, 64)):
    path = TEXTURE_PATHS.get(name)

    if not path:
        raise ValueError(f'Nie znaleziono tekstury "{name}"')
    
    if name not in texture_cache:
        texture_cache[name] = load_texture_file(path)

    texture = texture_cache[name]

    if size:
        texture = pg.transform.scale(texture, size)

    return texture


def get_sprites(sheet_name: str, sprite_name: str, size: tuple=(64, 64)):
    sheet_info = SPRITE_SHEET_PATHS.get(sheet_name)

    if not sheet_info:
        raise ValueError(f'Nie znaleziono sprite sheet "{sheet_name}"')
    
    path = sheet_info.get('path')
    
    if sheet_name not in texture_cache:
        texture_cache[sheet_name] = load_texture_file(path)

    sheet = texture_cache[sheet_name]
    frame_width, frame_height, num_frames, row, flip_vert = sheet_info.get(sprite_name)
    sprites = []

    for x in range(num_frames):
        frame = sheet.subsurface((x * frame_width, row * frame_height, frame_width, frame_height))

        if size:
            frame = pg.transform.scale(frame, size)

        if flip_vert:
            frame = pg.transform.flip(frame, flip_x=flip_vert, flip_y=False)

        sprites.append(frame)

    return sprites


    

