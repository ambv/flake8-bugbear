"""
Should emit:
B014 - on lines 10, 16, 27, 41, and 48
"""

import re

try:
    pass
except (Exception, TypeError):
    # TypeError is a subclass of Exception, so it doesn't add anything
    pass

try:
    pass
except (OSError, OSError) as err:
    # Duplicate exception types are useless
    pass


class MyError(Exception):
    pass


try:
    pass
except (MyError, MyError):
    # Detect duplicate non-builtin errors
    pass


try:
    pass
except (MyError, Exception) as e:
    # Don't assume that we're all subclasses of Exception
    pass


try:
    pass
except (MyError, BaseException) as e:
    # But we *can* assume that everything is a subclass of BaseException
    pass


try:
    pass
except (re.error, re.error):
    # Duplicate exception types as attributes
    pass
