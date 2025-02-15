from utils.textures_utils import get_texture

class Wood:
    def __init__(self, amount):
        self.name = 'wood'
        self.image = get_texture('wood', size=(64*2, 64*2))
        self.stackable = True
        self.amount = amount
        self.max_amount = 999