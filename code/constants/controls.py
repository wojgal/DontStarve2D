import pygame as pg

INPUT_MAPPING = {
    'move_up': [pg.K_UP, pg.K_w],
    'move_down': [pg.K_DOWN, pg.K_s],
    'move_left': [pg.K_LEFT, pg.K_a],
    'move_right': [pg.K_RIGHT, pg.K_d],
    'attack': [pg.K_SPACE],
    'interact': [pg.K_e],
    'inventory': [pg.K_i]
}