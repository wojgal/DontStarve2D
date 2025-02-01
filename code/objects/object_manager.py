from constants.objects import OBJECTS_PARAMETERS
from constants.tiles import TILE_SIZE
from objects.tree import Tree

class ObjectManager:
    def __init__(self, tilemap, noise):
        self.tilemap = tilemap
        self.noise = noise
        self.objects = []

        self.generate_objects()
        

    def generate_objects(self):
        '''Generuje obiekty na mapie (np. drzewo)'''
        world_size = self.tilemap.size

        for y in range(world_size):
            for x in range(world_size):
                perlin_value = self.noise([x / world_size, y / world_size])
                normalized_value = (perlin_value + 1) / 2

                # Generowanie drzew
                if normalized_value > OBJECTS_PARAMETERS['tree']['threshold'] and self.tilemap.get_tile(x, y).type == 'grass':
                    self.objects.append(Tree(x * TILE_SIZE, y * TILE_SIZE))


    def get_object_at(self, x, y):
        '''Zwraca obiekt na danej pozycji (lub None)
            Pozycja to konkretne piksele obiektu, nie grid!'''
        for object in self.objects:
            if object.rect.collidepoint(x, y):
                return object
            
        return None


    def remove_object(self, object):
        self.objects.remove(object)


    def update(self):
        pass


    def draw(self, screen):
        for object in self.objects:
            object.draw(screen)