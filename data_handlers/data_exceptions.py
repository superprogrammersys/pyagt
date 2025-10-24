"""
exceptions.py. a part of pyagt library
"""


class UnsupportedAlgorithm(Exception):
    """raised when the user tries supplying an algorithm not specified in constants"""
    pass
