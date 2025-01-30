import pygame as pg
from constants.paths import TEXTURE_PATHS, SPRITE_SHEET_PATHS

texture_cache = {}

def load_texture(path, size=None):
    '''Wczytuje grafikę z pliku'''
    image = pg.image.load(path).convert_alpha()

    if size:
        image = pg.transform.scale(image, size)

    return image


def get_texture(name, size=None):
    '''Pobiera grafikę z cache lub ładuje, jeśli jeszcze jej tam nie ma'''
    path = TEXTURE_PATHS.get(name)

    if not path:
        raise ValueError(f'Nie znaleziono tekstury "{name}"')
    
    if path not in texture_cache:
        texture_cache[path] = load_texture(path, size)

    return texture_cache[path]




#TODO TUTAJ ZROBIL SIE SYF Z TYM SPRITE SHEET OGARNAC TO JUTRO

def load_sprite_sheet():
    pass


def get_texture_from_sprite_sheet():
    pass

def get_sprite_sheet(name):
    path = SPRITE_SHEET_PATHS.get(name)

    if not path:
        raise ValueError(f'Nie znaleziono tekstury (sprite) "{name}"')
    
    if path not in texture_cache:
        texture_cache[path] = load_sprite_sheet(path)

    return texture_cache[path]