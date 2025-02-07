import pygame as pg
from world.world import World
from entities.player import Player
from constants import colors

class GameScene:
    def __init__(self, game):
        self.game = game

        self.world = World()
        self.player = Player(10, 10, self.world)


    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    self.game.change_scene('menu')

        self.player.handle_events(events)

    def update(self, dt):
        self.player.update(dt)

    def draw(self, screen):
        screen.fill(colors.BLACK)

        self.world.draw(screen)
        self.player.draw(screen)
