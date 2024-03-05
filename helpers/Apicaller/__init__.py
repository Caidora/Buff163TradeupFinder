import json
import os
import pathlib
import sys
from . import exceptions
from . import retrieveJson
from .exceptions import BuffError
from .retrieveJson import Buff

if getattr(sys, 'frozen', False):
    # https://pyinstaller.org/en/stable/runtime-information.html
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    base_path = pathlib.Path(sys.executable).parent  # noqa
else:
    base_path = pathlib.Path(os.path.abspath(__file__)).parent.parent

config_path = os.path.join(base_path, 'json/config.json')
print(config_path)
config = json.load(open(config_path))
