import pygame as pg
from constants.paths import MUSIC_PATHS, SFX_PATHS

class AudioManager:
    def __init__(self, music_volume=0.5, sfx_volume=0.5):
        pg.mixer.init()
        self.music_volume = music_volume
        self.music_enabled = True

        self.sfx_volume = sfx_volume
        self.sfx_enabled = True
        self.sfx = {}


        self.fade_ms = 1000


    def play_music(self, music_name, loops=-1):
        if not self.sfx_enabled:
            return
        
        if music_name in MUSIC_PATHS:
            pg.mixer.music.fadeout(self.fade_ms)
            pg.mixer.music.load(MUSIC_PATHS[music_name])
            pg.mixer.music.set_volume(self.music_volume)
            pg.mixer.music.play(loops=loops, fade_ms=self.fade_ms)


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


    def set_music_volume(self, volume):
        self.music_volume = volume
        pg.mixer.music.set_volume(self.music_volume)


    def set_sfx_volume(self, volume):
        self.sfx_volume = volume

        for sfx in self.sfx:
            sfx.set_volume(self.sfx_volume)