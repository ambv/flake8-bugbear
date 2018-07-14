import collections
import logging
import time


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


def do_this_instead(value=None):
    if value is None:
        value = set()


def in_fact_all_calls_are_wrong(value=time.time()):
    ...


LOGGER = logging.getLogger(__name__)


def do_this_instead_of_calls_in_defaults(logger=LOGGER):
    # That makes it more obvious that this one value is reused.
    ...
