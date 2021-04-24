# Ownership information
__author__ = 'Imam Hossain Roni'
__copyright__ = "Copyright 2021, Roni"
__credits__ = ["Roni"]
__license__ = "MIT"
__version__ = "1.0.3"
__maintainer__ = "Roni"
__email__ = "imamhossainroni95@gmail.com"
__status__ = "Development"

from enum import IntEnum


class Choice(IntEnum):
    def __init__(self, *args):
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name

            raise ValueError("aliases not allowed in DuplicateFreeEnum:  %r --> %r" % (a, e))

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]