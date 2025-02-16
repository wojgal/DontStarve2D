import pygame as pg
from constants.colors import BLACK, RED, WHITE
from constants.scenes import MENU_SCENE
from ui.text import draw_text

class SettingsScene:
    def __init__(self, game):
        self.game = game

        self.options = [
            ('Muzyka', None),
            ('Dzwieki', None)
        ]

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
                    pass

                elif event.key in (pg.K_LEFT, pg.K_a):
                    pass

                elif event.key in (pg.K_RETURN, pg.K_SPACE):
                    option_name, option_action = self.options[self.selected_option]
                    # Tutaj trzeba sprawdzic jak wykonac funkcje ktora sie znajduje w option action

                elif event.key == pg.K_ESCAPE:
                    self.game.change_scene(MENU_SCENE)


    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill(BLACK)

        for idx, option in enumerate(self.options):
            option_name, option_action = option

            if idx == self.selected_option:
                draw_text(screen=screen, text=option_name, x='center', y=100 + idx * self.text_spacing, size=self.font_size, color=RED)
            else:
                draw_text(screen=screen, text=option_name, x='center', y=100 + idx * self.text_spacing, size=self.font_size, color=WHITE)

