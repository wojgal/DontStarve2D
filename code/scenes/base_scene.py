class BaseScene:
    def __init__(self, game):
        self.game = game    # Referencja do obiektu gry
        
    def hanlde_events(self, events):
        """Obsługa zdarzeń"""
        pass

    def update(self):
        """Logika gry"""
        pass

    def draw(self, screen):
        """Rysowanie na ekranie"""
        pass