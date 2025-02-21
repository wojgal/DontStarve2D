import pygame as pg
from constants.paths import MUSIC_PATHS, SFX_PATHS


class AudioManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AudioManager, cls).__new__(cls)
            cls._instance._initialized = False

        return cls._instance
    

    def __init__(self):
        if not self._initialized:
            pg.mixer.init()
            self.sfx = {}
            self.fade_ms = 1000
            self.in_de_step = 0.05
            self._initialized = True

    
    def load_settings(self, settings):
        self.music_enabled = settings.get('MUSIC_ENABLED')
        self.music_volume = settings.get('MUSIC_VOLUME')

        self.sfx_enabled = settings.get('SFX_ENABLED')
        self.sfx_volume = settings.get('SFX_VOLUME')


    def play_music(self, music_name, loops=-1):
        if music_name in MUSIC_PATHS:
            pg.mixer.music.fadeout(self.fade_ms)
            pg.mixer.music.load(MUSIC_PATHS[music_name])
            pg.mixer.music.set_volume(self.music_volume)
            pg.mixer.music.play(loops=loops, fade_ms=self.fade_ms)

        if not self.music_enabled:
            pg.mixer.music.pause()


    def pause_music(self):
        pg.mixer.music.pause()


    def resume_music(self):
        pg.mixer.music.unpause()


    def stop_music(self):
        pg.mixer.music.stop()


    def toggle_music(self):
        self.music_enabled = not self.music_enabled

        if self.music_enabled:
            pg.mixer.music.unpause()
        else:
            pg.mixer.music.pause()

        return self.music_enabled
    

    def increase_music_volume(self):
        self.music_volume = min(1.0, self.music_volume + self.in_de_step)
        pg.mixer.music.set_volume(self.music_volume)

        return round(self.music_volume, 2)


    def decrease_music_volume(self):
        self.music_volume = max(0.0, self.music_volume - self.in_de_step)
        pg.mixer.music.set_volume(self.music_volume)

        return round(self.music_volume, 2)


    # def set_music_volume(self, volume):
    #     self.music_volume = volume
    #     pg.mixer.music.set_volume(self.music_volume)


    def play_sfx(self, sfx_name):
        if not self.sfx_enabled:
            return
        
        if sfx_name not in self.sfx and sfx_name in SFX_PATHS:
            self.sfx[sfx_name] = pg.mixer.Sound(SFX_PATHS[sfx_name])
            self.sfx[sfx_name].set_volume(self.sfx_volume)

        if sfx_name in self.sfx:
            self.sfx[sfx_name].play()


    def toggle_sfx(self):
        self.sfx_enabled = not self.sfx_enabled

        return self.sfx_enabled
    

    def increase_sfx_volume(self):
        self.sfx_volume = min(1.0, self.sfx_volume + self.in_de_step)

        for sfx in self.sfx.values():
            sfx.set_volume(self.sfx_volume)

        return round(self.sfx_volume, 2)


    def decrease_sfx_volume(self):
        self.sfx_volume = max(0.0, self.sfx_volume - self.in_de_step)

        for sfx in self.sfx.values():
            sfx.set_volume(self.sfx_volume)

        return round(self.sfx_volume, 2)


    # def set_sfx_volume(self, volume):
    #     self.sfx_volume = volume

    #     for sfx in self.sfx:
    #         sfx.set_volume(self.sfx_volume)


AUDIO_MANAGER = AudioManager()