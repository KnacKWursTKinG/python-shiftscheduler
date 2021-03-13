
import sys

from threading import Thread
from os import system

from .config import c
from .backend import App


def entry_point():
    if c.platform == 'ubuntu-phablet':
        import socket

        sock = socket.socket()
        sock.bind((c.ini.get('flask', 'host'), c.ini.getint('flask', 'port')))
        port = sock.getsockname()[1]
        sock.close()

        thread = Thread(target=App.run, kwargs={'port': port}, daemon=True)
        thread.start()

        system("webapp-container 'http://localhost:{}/'".format(port))
        sys.exit(0)

    elif c.platform == 'Linux':
        import logging
        import webview

        App.logger.level = logging.DEBUG
        webview.create_window("Shift Scheduler", App)
        webview.start(debug=True, gui="qt")
