"""
Should emit:
B301 - on lines 39-42
B302 - on lines 43-46
B305 - on lines 47-48
"""

import builtins  # future's builtins really
import future.utils
import six
from six import iterkeys
from future.utils import itervalues


def this_is_okay():
    d = {}
    iterkeys(d)
    six.iterkeys(d)
    six.itervalues(d)
    six.iteritems(d)
    six.iterlists(d)
    six.viewkeys(d)
    six.viewvalues(d)
    six.viewlists(d)
    itervalues(d)
    future.utils.iterkeys(d)
    future.utils.itervalues(d)
    future.utils.iteritems(d)
    future.utils.iterlists(d)
    future.utils.viewkeys(d)
    future.utils.viewvalues(d)
    future.utils.viewlists(d)
    six.next(d)
    builtins.next(d)


def everything_else_is_wrong():
    d = None  # note: bugbear is no type checker
    d.iterkeys()
    d.itervalues()
    d.iteritems()
    d.iterlists()  # Djangoism
    d.viewkeys()
    d.viewvalues()
    d.viewitems()
    d.viewlists()  # Djangoism
    d.next()
    d.keys().next()
