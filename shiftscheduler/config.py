
import os

from configparser import ConfigParser
from datetime import date


_APPNAME = 'shiftscheduler'
_CREATOR = 'knackwurstking'


def get_platform() -> str:
    sysname, nodename, _, _, _ = os.uname()

    if nodename not in ['ubuntu-phablet']:
        nodename = None

    return nodename or sysname


def save_user_config():
    # create dirs to config if not exists
    if not os.path.exists(c.get_path('config')):
        os.makedirs(c.get_path('config'))

    with open(c.get_path('config') + '/config.ini', 'w') as file:
        c.ini.write(file)


def load_configs():
    c.ini.read([__file__.rsplit('/', 1)[0] + '/config.ini', c.get_path('config') + '/config.ini'])

    # parse config
    c.steps = c.ini.get('shiftscheduler', 'steps', fallback='').strip().split(',')
    c.optional_steps = list(c.ini.get('shiftscheduler', 'opt_steps', fallback='').strip().split(','))

    try:
        # remove '0' from date (Ex. 2021/02/01 -> 2021/2/1)
        start_date = None
        start_date = list(
            map(
                int,
                c.ini.get(
                    'shiftscheduler',
                    'start_date',
                    fallback=''
                ).strip().split('/')
            )
        )
    except ValueError:
        pass

    c.start_date = date(*start_date) if start_date else None


class c():
    platform: str = get_platform()
    ini: ConfigParser = ConfigParser()

    path: dict = {
        'ubuntu-phablet': {
            'config': os.path.expanduser('~/.config/{}.{}'.format(_APPNAME, _CREATOR)),
            'cache': os.path.expanduser('~/.cache/{}.{}'.format(_APPNAME, _CREATOR)),
            'share': os.path.expanduser('~/.local/share/{}.{}'.format(_APPNAME, _CREATOR))
        }, 'Linux': {
            'config': os.path.expanduser('~/.config/{}'.format(_APPNAME)),
            'cache': os.path.expanduser('~/.cache/{}'.format(_APPNAME)),
            'share': os.path.expanduser('~/.local/share/{}'.format(_APPNAME))
        }
    }

    steps: list = list()
    optional_steps = list()
    start_date: date = None

    @classmethod
    def get_path(cls, path: str) -> str:
        return cls.path[cls.platform][path]


load_configs()
