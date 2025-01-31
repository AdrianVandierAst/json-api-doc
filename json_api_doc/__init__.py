# -*- coding: utf-8 -*-

__author__ = """Julien Duponchelle"""
__email__ = 'julien@duponchelle.info'
__version__ = '0.9.0'


from .serialization import serialize
from .deserialization import deserialize, _flat, _resolve, _parse_included

# keeps backwards compatibility
parse = deserialize

__all__ = ['serialize', 'deserialize', '_flat', '_resolve', '_parse_included']
