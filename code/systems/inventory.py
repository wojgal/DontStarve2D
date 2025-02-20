import pygame as pg
from utils.textures_utils import get_texture

class Inventory:
    def __init__(self):
        self.width = 4
        self.height = 4
        self.capacity = self.width * self.height
        self.slot_size = 128
        self.start_x = 660 + 32
        self.start_y = 240 + 32

        self.items = [None for _ in range(self.capacity)]

        self.is_open = False
        self.image = get_texture('inventory', size=(600, 600))
        self.rect = self.image.get_rect(topleft=(660, 240))


    def add_item(self, new_item):
        for item in self.items:
            if item != new_item:
                continue

            item_capacity = item.get_capacity()

            if item_capacity == 0:
                continue

            if new_item.amount > item_capacity:
                item.amount += item_capacity
                new_item.amount -= item_capacity
            else:
                item.amount += new_item.amount
                new_item.amount = 0
            
            if new_item.amount == 0:
                break

        else:
            free_slot_idx = self.items.index(None)
            self.items[free_slot_idx] = new_item


    def toggle_open(self):
        self.is_open = not self.is_open


    def update(self):
        pass


    def draw(self, screen):
        if self.is_open:
            screen.blit(self.image, self.rect)

            for idx, item in enumerate(self.items):
                if item == None:
                    continue
                
                x = self.start_x + (idx % self.width) * (self.slot_size + 8)
                y = self.start_y + (idx // self.height) * (self.slot_size + 8)
                
                item.draw(screen, x, y)

    