import pygame as pg
from systems.window import WINDOW_MANAGER
from systems.audio import AUDIO_MANAGER
from systems.settings import SETTINGS
from constants.settings_scene import SETTINGS_SCENE_OPTIONS
from constants.colors import BLACK, RED, WHITE
from constants.scenes import MENU_SCENE
from ui.text import draw_text

class SettingsScene:
    def __init__(self, game):
        self.game = game
        self.window = WINDOW_MANAGER
        self.audio_manager = AUDIO_MANAGER
        self.settings = SETTINGS

        self.options = SETTINGS_SCENE_OPTIONS

        self.selected_option = 0
        self.text_spacing = 100
        self.font_size = 100


    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:

                if event.key in (pg.K_UP, pg.K_w):
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                
                elif event.key in (pg.K_DOWN, pg.K_s):
                    self.selected_option = (self.selected_option + 1) % len(self.options)

                elif event.key in (pg.K_RIGHT, pg.K_d):
                    option = self.options[self.selected_option]
                    function = option['increase']
                    
                    if function is not None:
                        new_state = function()
                        self.settings.set(option['key'], new_state)

                elif event.key in (pg.K_LEFT, pg.K_a):
                    option = self.options[self.selected_option]
                    function = option['decrease']

                    if function is not None:
                        new_state = function()
                        self.settings.set(option['key'], new_state)

                elif event.key in (pg.K_RETURN, pg.K_SPACE):
                    option = self.options[self.selected_option]
                    function = option['action']

                    if function is not None:
                        new_state = function()
                        self.settings.set(option['key'], new_state)

                elif event.key == pg.K_ESCAPE:
                    self.game.change_scene(MENU_SCENE)
                    self.selected_option = 0


    def update(self, dt):
        pass


    def draw(self, screen):
        screen.fill(BLACK)

        for idx, option in enumerate(self.options):
            state = self.settings.get(option['key'])
            text = f'{option['label']}   {state}'

            if idx == self.selected_option:
                draw_text(screen=screen, text=text, x='center', y=100 + idx * self.text_spacing, size=self.font_size, color=RED)
            else:
                draw_text(screen=screen, text=text, x='center', y=100 + idx * self.text_spacing, size=self.font_size, color=WHITE)

