from constants.objects import OBJECTS_PARAMETERS
from constants.tiles import TILE_SIZE
from objects.tree import Tree

class ObjectManager:
    def __init__(self, tilemap, noise):
        self.tilemap = tilemap
        self.noise = noise
        self.camera = None
        self.objects = {}

        self.generate_objects()
    

    def generate_objects(self):
        '''Generuje obiekty na mapie (np. drzewo)'''
        world_size = self.tilemap.size

        for y in range(world_size):
            for x in range(world_size):
                new_object = None
                perlin_value = self.noise([x / world_size, y / world_size])
                normalized_value = (perlin_value + 1) / 2

                # Generowanie drzew
                if normalized_value > OBJECTS_PARAMETERS['tree']['threshold'] and self.tilemap.get_tile(x, y).type == 'grass':
                    new_object = Tree(x, y)

                if new_object is not None:
                    self.objects[(x, y)] = new_object


    def get_object_at(self, x, y):
        '''Zwraca obiekt na danym kafelku (lub None)'''
        #print(self.objects[(x, y)].type)
        return self.objects.get((x, y))


    def remove_object(self, object):
        self.objects.pop((object.rect.x // TILE_SIZE, object.rect.y // TILE_SIZE))


    def update(self):
        pass


    def draw(self, screen):
        start_tile_x, start_tile_y, end_tile_x, end_tile_y = self.camera.get_tiles_range()
        offset_x, offset_y = self.camera.get_offset()

        for x in range(start_tile_x, end_tile_x):
            for y in range(start_tile_y, end_tile_y):
                object = self.get_object_at(x, y)

                if object is None:
                    continue

                object.draw(screen, offset_x, offset_y)