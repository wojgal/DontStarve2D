import pygame as pg
from numpy.random import randint
from constants.world import WORLD_SIZE
from world.tilemap import TileMap
from perlin_noise import PerlinNoise
from objects.object_manager import ObjectManager

class World:
    def __init__(self):
        self.camera = None
        self.noise = PerlinNoise(octaves=4, seed=randint(1000))
        self.tilemap = TileMap(WORLD_SIZE, self.noise)
        self.object_manager = ObjectManager(self.tilemap, self.noise)
    

    def update(self, dt):
        pass


    def draw(self, screen):
        self.tilemap.draw(screen)
        self.object_manager.draw(screen)


    def get_tile(self, x, y):
        return self.tilemap.get_tile(x, y)

    def get_object_at(self, x, y):
        return self.object_manager.get_object_at(x, y)
    
    def remove_object(self, object):
        self.object_manager.remove_object(object)

    def set_camera(self, camera):
        self.camera = camera
        self.tilemap.camera = camera
        self.object_manager.camera = camera


