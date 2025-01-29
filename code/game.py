import pygame as pg
from settings import Settings
from scenes.menu_scene import MenuScene

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode(self.settings.get('RESOLUTION'))
        self.clock = pg.time.Clock()
        self.running = True
        self.scenes = {
            'menu': MenuScene(self)
        }

        self.current_scene =  self.scenes['menu']

    def change_scene(self, scene_name):
        if scene_name is None:
            return
        
        if scene_name == 'quit':
            self.running = False
            return

        self.current_scene = self.scenes[scene_name]

    def run(self):
        while self.running:
            events = pg.event.get()

            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
                    
            self.current_scene.handle_events(events)
            self.current_scene.update()
            self.current_scene.draw(self.screen)

            pg.display.update()
            self.clock.tick(self.settings.get('FPS'))


        pg.quit()
