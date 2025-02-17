import pygame as pg
from world.world import World
from entities.player import Player
from systems.camera import Camera
from constants import colors
from constants.world import WORLD_SIZE
from constants.scenes import MENU_SCENE

class GameScene:
    def __init__(self, game):
        self.game = game
        self.audio_manager = game.audio_manager

        self.world = World(self.audio_manager)
        self.player = Player(WORLD_SIZE // 2, WORLD_SIZE // 2, self.world)
        self.camera = Camera(self.player, self.game.settings.get('SCREEN_WIDTH'), self.game.settings.get('SCREEN_HEIGHT'))

        self.world.set_camera(self.camera)
        self.player.set_cammera(self.camera)


    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    self.game.change_scene(MENU_SCENE)

        self.player.handle_events(events)


    def update(self, dt):
        self.player.update(dt)
        self.world.update(dt)


    def draw(self, screen):
        screen.fill(colors.BLACK)

        self.world.draw(screen)
        self.player.draw(screen)
