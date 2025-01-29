import pygame as pg
from constants import colors
from math import sqrt

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)
        self.speed = 4

    def move(self, dx, dy):
        # Poruszanie po przekatnej
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
    def handle_input(self, keys):
        dx, dy = 0, 0
        # Ruch gracza w górę (klawisze strzałki w górę lub W)
        if keys[pg.K_UP] or keys[pg.K_w]:
            dy -= 1
        # Ruch gracza w lewo (klawisze strzałki w lewo lub A)
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            dx -= 1
        # Ruch gracza w dół (klawisze strzałki w dół lub S)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            dy += 1
        # Ruch gracza w prawo (klawisze strzałki w prawo lub D)
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            dx += 1

        self.move(dx, dy)
    
    def draw(self, screen):
        pg.draw.rect(screen, colors.RED, self.rect)