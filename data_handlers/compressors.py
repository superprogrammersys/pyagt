"""
compressors.py. a part of pyagt library
"""
import lzma
import zlib
import bz2
from .data_exceptions import UnsupportedAlgorithm


ZLIB = 'zlib'
BZ2 = 'bz2'
LZMA = 'lzma'

def data_compress(data, algorithm=ZLIB, compression_level=6):
    """
    compress the data
    args:
    data(bytes)
    algorithm(default is ZLIB)
    compression_level(int=6)

    """
    if not isinstance(data, bytes):
        data = data.encode()
    if algorithm is ZLIB:
        return zlib.compress(data, level=compression_level)
    elif algorithm is LZMA:
        return lzma.compress(data, preset=compression_level)
    elif algorithm is BZ2:
        return bz2.compress(data, compresslevel=compression_level)
    else:
        raise UnsupportedAlgorithm

def data_decompress(data, algorithm=ZLIB):
    """
    decompress the data
    args:
    data(bytes)
    algorithm=ZLIB
    """
    if not isinstance(data, bytes):
        data = data.encode()
    if algorithm is ZLIB:
        return zlib.decompress(data)
    elif algorithm is LZMA:
        return lzma.decompress(data)
    elif algorithm is BZ2:
        return bz2.decompress(data)
    else:
        raise UnsupportedAlgorithm('use known algorithm')
