#!/usr/bin/python3
""" this is a new instance variable of models"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
