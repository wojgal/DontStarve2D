import pygame as pg
from utils.textures_utils import get_texture

class Inventory:
    def __init__(self):
        self.items = {}
        self.capacity = 10
        self.is_open = False
        self.image = get_texture('inventory', size=(600, 600))
        self.rect = self.image.get_rect(topleft=(660, 240))


    def add_item(self, item):
        item_name = item.name

        if self.items.get(item_name):
            self.items[item_name].amount += item.amount

        else:
            if len(self.items) < self.capacity:
                self.items[item_name] = item


    def toggle_open(self):
        self.is_open = not self.is_open


    def update(self):
        pass


    def draw(self, screen):
        if self.is_open:
            screen.blit(self.image, self.rect)

        for item_name, item in self.items.items():
            print(item_name, item.amount)

    