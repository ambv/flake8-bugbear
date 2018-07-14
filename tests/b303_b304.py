"""
Should emit:
B303 - on line 21
B304 - on line 38
"""

import sys
import something_else


def this_is_okay():
    something_else.maxint
    maxint = 3
    maxint


maxint = 3


def this_is_also_okay():
    maxint


class CustomClassWithBrokenMetaclass:
    __metaclass__ = type
    maxint = 5  # this is okay
    # the following shouldn't crash
    (a, b, c) = list(range(3))
    # it's different than this
    a, b, c = list(range(3))
    a, b, c, = list(range(3))
    # and different than this
    (a, b), c = list(range(3))
    a, *b, c = [1, 2, 3, 4, 5]
    b[1:3] = [0, 0]

    def this_is_also_fine(self):
        self.maxint


def this_is_wrong():
    sys.maxint
