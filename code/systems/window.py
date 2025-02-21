import pygame as pg
from constants.window import RESOLUTIONS


class WindowManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WindowManager, cls).__new__(cls)
            cls._instance._initialized = False

        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            pg.display.set_caption('Game')
            self.screen = None
            self.resolution_types = RESOLUTIONS

            self._initialized = True


    def update_screen(self):
        flags = pg.FULLSCREEN if self.fullscreen else 0
        self.screen = pg.display.set_mode(self.resolution, flags)


    def load_settings(self, settings):
        self.resolution = settings.get('RESOLUTION')
        self.fullscreen = settings.get('FULLSCREEN')
        self.update_screen()


    def increase_resolution(self):
        current_resolution_idx = self.resolution_types.index(tuple(self.resolution))
        new_resolution_idx = min(len(self.resolution_types) - 1, current_resolution_idx + 1)
        self.resolution = self.resolution_types[new_resolution_idx]
        self.update_screen()
        return self.resolution


    def decrease_resoltuioon(self):
        current_resolution_idx = self.resolution_types.index(tuple(self.resolution))
        new_resolution_idx = max(0, current_resolution_idx - 1)
        self.resolution = self.resolution_types[new_resolution_idx]
        self.update_screen()
        return self.resolution


    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.update_screen()
        return self.fullscreen


WINDOW_MANAGER = WindowManager()
    