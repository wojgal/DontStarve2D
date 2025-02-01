import pygame as pg
from world.world import World
from entities.player import Player
from constants import colors

class GameScene:
    def __init__(self, game):
        self.game = game

        self.world = World()
        self.player = Player(384, 384, 64, 64, self.world)


    def handle_events(self, events):
        keys = pg.key.get_pressed()

        for event in events:
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    self.game.change_scene('menu')

        self.player.handle_input(keys)

    def update(self, dt):
        self.player.update(dt)

    def draw(self, screen):
        screen.fill(colors.BLACK)

        self.world.draw(screen)
        self.player.draw(screen)
