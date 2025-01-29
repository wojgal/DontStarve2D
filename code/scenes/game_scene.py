import pygame as pg
from world.world import World
from entities.player import Player
from constants import colors

class GameScene:
    def __init__(self, game):
        self.game = game

        self.world = World()
        self.player = Player(400, 400, 64, 64)


    def handle_events(self, events):
        keys = pg.key.get_pressed()
        self.player.handle_input(keys)

        for event in events:
            pass

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(colors.BLACK)

        self.world.draw(screen)
        self.player.draw(screen)
