import collections
import logging
import time
import types
from types import MappingProxyType


def this_is_okay(value=(1, 2, 3)):
    ...


def and_this_also(value=tuple()):
    pass


def frozenset_also_okay(value=frozenset()):
    pass


def mappingproxytype_okay(
    value=MappingProxyType({}), value2=types.MappingProxyType({})
):
    pass


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


def kwonlyargs_immutable(*, value=()):
    ...


def kwonlyargs_mutable(*, value=[]):
    ...
