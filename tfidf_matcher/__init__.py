# -*- coding: utf-8 -*-

from .ngrams import ngrams
from .matcher import matcher

__all__ = ['ngrams','matcher']

# version as tuple for simple comparisons
VERSION = (0, 1, 1)
# string created from tuple to avoid inconsistency
__version__ = ".".join([str(x) for x in VERSION])
