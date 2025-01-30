import pygame as pg
from constants import colors
from constants.paths import FONT_PATHS

def draw_text(screen, text, x, y, size=24, color=colors.WHITE):
    '''Rysowanie tekstu na ekranie'''
    font = pg.font.Font(FONT_PATHS['main'], size)
    text_surface = font.render(text, True, color)

    if x == 'center':
        new_x = (screen.get_width() - text_surface.get_width()) // 2
    else:
        new_x = x

    if y == 'center':
        new_y = (screen.get_height() - text_surface.get_height()) // 2
    else:
        new_y = y

    screen.blit(text_surface, (new_x, new_y))