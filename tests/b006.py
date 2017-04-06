import collections


def this_is_okay(value=(1, 2, 3)):
    ...


def this_is_wrong(value=[1, 2, 3]):
    ...


def this_is_also_wrong(value={}):
    ...


def and_this(value=set()):
    ...


def this_too(value=collections.OrderedDict()):
    ...

async def async_this_too(value=collections.OrderedDict()):
    ...

def but_that_is_okay(value=tuple()):
    ...


def do_this_instead(value=None):
    if value is None:
        value = set()
