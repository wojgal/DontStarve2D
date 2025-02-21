from systems.window import WINDOW_MANAGER
from systems.audio import AUDIO_MANAGER

BLANK_SPACE = {
    'label': '',
    'key': None,
    'action': None,
    'increase': None,
    'decrease': None,
}


SETTINGS_SCENE_OPTIONS =[
    {
        'label': 'Muzyka',
        'key': 'MUSIC_ENABLED',
        'action': AUDIO_MANAGER.toggle_music,
        'increase': None,
        'decrease': None,
    },
    {
        'label': 'Glosnosc muzyki',
        'key': 'MUSIC_VOLUME',
        'action': None,
        'increase': AUDIO_MANAGER.increase_music_volume,
        'decrease': AUDIO_MANAGER.decrease_music_volume,
    },
    {
        'label': 'Dzwieki',
        'key': 'SFX_ENABLED',
        'action': AUDIO_MANAGER.toggle_sfx,
        'increase': None,
        'decrease': None,
    },
    {
        'label': 'Glosnosc dzwiekow',
        'key': 'SFX_VOLUME',
        'action': None,
        'increase': AUDIO_MANAGER.increase_sfx_volume,
        'decrease': AUDIO_MANAGER.decrease_sfx_volume,
    },
    {
        'label': 'Rozdzielczosc',
        'key': 'RESOLUTION',
        'action': None,
        'increase': WINDOW_MANAGER.increase_resolution,
        'decrease': WINDOW_MANAGER.decrease_resoltuioon,
    },
    {
        'label': 'Pelny ekran',
        'key': 'FULLSCREEN',
        'action': WINDOW_MANAGER.toggle_fullscreen,
        'increase': None,
        'decrease': None,
    },
]