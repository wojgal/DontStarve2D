import pygame as pg
from utils.textures_utils import get_texture
from ui.text import draw_text

class Wood:
    def __init__(self, amount):
        self.name = 'wood'
        self.image = get_texture('wood', size=(64*2, 64*2))
        self.stackable = True
        self.amount = amount
        self.max_amount = 10


    def get_capacity(self):
        return self.max_amount - self.amount


    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

        if self.amount > 1:
            draw_text(screen, str(self.amount), x + 64, y + 64)


    def __eq__(self, other):
        if other is None:
            return False
        
        return self.name == other.name
        
        
        