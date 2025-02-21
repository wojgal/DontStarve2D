import pygame as pg
from systems.audio import AUDIO_MANAGER
from constants.colors import BLACK, WHITE, RED
from constants.scenes import GAME_SCENE, QUIT, SETTINGS_SCENE
from ui.text import draw_text

class MenuScene:
    def __init__(self, game):
        self.game = game
        self.audio_manager = AUDIO_MANAGER
        self.audio_manager.play_music('music')

        # Opcje, (nazwa, scena)
        self.options = [
            ('Nowa Gra', GAME_SCENE),
            ('Opcje', SETTINGS_SCENE),
            ('Wyjdz', QUIT)
        ]
        self.selected_option = 0
        self.font_size = 100
        self.text_spacing = 100


    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:

                # Przesuwanie po menu w góre za pomocą strzałki w górę lub klawisza 'w'
                if event.key == pg.K_UP or event.key == pg.K_w:
                    self.selected_option = (self.selected_option - 1) % len(self.options)

                # Przesuwanie po menu w dół za pomocą strzałki w dół lub klawisza 's'
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    self.selected_option = (self.selected_option + 1) % len(self.options)

                # Wybór opcji za pomocą klawisza Enter lub spacji
                elif event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                    option_name, option_scene = self.options[self.selected_option]
                    self.game.change_scene(option_scene)
                    self.selected_option = 0


    def update(self, dt):
        pass


    def draw(self, screen):
        screen.fill(BLACK)

        for idx, option in enumerate(self.options):
            option_name, option_scene = option

            if idx == self.selected_option:
                draw_text(screen=screen, text=option_name, x='center', y=100 + idx * self.text_spacing, size=self.font_size, color=RED)
            else:
                draw_text(screen=screen, text=option_name, x='center', y=100 + idx * self.text_spacing, size=self.font_size, color=WHITE)



