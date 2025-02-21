import json
import os

# Domyślne ustawienia gry
DEFAULT_SETTINGS = {
    'RESOLUTION': (1920, 1080),
    'FULLSCREEN': False,
    'FPS': 60,
    'MUSIC_ENABLED': True,
    'MUSIC_VOLUME': 0.5,
    'SFX_ENABLED': True,
    'SFX_VOLUME': 0.5
}

class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance._initialized = False

        return cls._instance
    

    def __init__(self, filename='settings.json'):
        if not self._initialized:
            self.filename = filename
            self.settings = DEFAULT_SETTINGS.copy()
            self.load_settings()

            self._initialized = True


    def load_settings(self):
        '''Wczytuje ustawienia z pliku, jeśli istnieje. W przeciwnym przypadku zostaje przy domyślnych.'''
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.settings.update(json.load(file))
            except json.JSONDecodeError:
                print('Błąd odczytu pliku z ustawieniami, używam domyślnych.')

        print(self.settings)


    def save_settings(self):
        '''Zapisuje aktualne ustawienia do pliku.'''
        with open(self.filename, 'w') as file:
            json.dump(self.settings, file)


    def get(self, key):
        '''Pobiera wartość ustawienia o podanej nazwie.'''
        return self.settings.get(key, DEFAULT_SETTINGS.get(key))
    
    
    def set(self, key, value):
        '''Ustawia wartość ustawienia o podanej nazwie.'''
        self.settings[key] = value


SETTINGS = Settings()
