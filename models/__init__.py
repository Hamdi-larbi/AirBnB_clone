#!/usr/bin/python3

"""storage unique instance for models directory"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
