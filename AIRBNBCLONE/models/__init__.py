#!/usr/bin/python3
"""This module initializes the models package"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()
storage.reload()