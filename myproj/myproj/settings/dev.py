from myproj.settings.base import *

DEBUG = True

try:
    from myproj.settings.local import *
except ImportError:
    pass
