import json
import os

# Domyślne ustawienia gry
DEFAULT_SETTINGS = {
    'SCREEN_WIDTH': 1280,
    'SCREEN_HEIGHT': 720,
    'RESOLUTION': (1280, 720),
    'FPS': 60
}

class Settings:
    def __init__(self, filename='settings.json'):
        self.filename = filename
        self.settings = DEFAULT_SETTINGS.copy()
        self.load_settings()

    def load_settings(self):
        '''Wczytuje ustawienia z pliku, jeśli istnieje. W przeciwnym przypadku zostaje przy domyślnych.'''
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.settings.update(json.load(file))
            except json.JSONDecodeError:
                print('Błąd odczytu pliku z ustawieniami, używam domyślnych.')

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
        self.save_settings()