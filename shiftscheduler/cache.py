
import os
import pickle

from .config import c


class CacheHandler():
    """ Caching for custom user data """
    data = {}
    ''' Ex.:
    data = {
        "YYYY/MM/DD": {
            "step": "...",
            "note": "..."
        }
    }
    '''

    def __init__(self, auto_store: bool = True):
        self.auto_store = auto_store

    def get(self, _date: str) -> dict:
        return self.data.get(_date, {'step': str(), 'note': None})

    def set(self, _date: str, **kwargs) -> None:
        self.data[_date] = {**self.get(_date), **kwargs}

        if self.auto_store:
            self.store()

    def unset(self, _date: str) -> None:
        del self.data[_date]

        if self.auto_store:
            self.store()

    def store(self) -> None:
        """ Save data in cache path (format: pickle) """
        cache = c.get_path('cache')
        path = cache + '/data.pickle'

        if not os.path.isdir(cache):
            os.makedirs(cache)

        with open(path, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self) -> None:
        """ Data will be load into self.data """
        path = c.get_path('cache') + '/data.pickle'

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                self.data = pickle.load(file)


Cache = CacheHandler()
Cache.load()
