from constants.paths import TEXTURE_PATHS
from utils.textures_utils import get_texture

TILE_SIZE = 64

TILE_TYPES = {
    'grass': {'walkable': True, 'texture': get_texture('grass')},
    'water': {'walkable': False, 'texture': get_texture('water')},
}