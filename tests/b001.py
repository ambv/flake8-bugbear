"""
Should emit:
B001 - on lines 8, 40, and 54
"""

try:
    import something
except:
    # should be except ImportError:
    import something_else as something

try:
    pass
except ValueError:
    # no warning here, all good
    pass

try:
    pass
except (KeyError, IndexError):
    # no warning here, all good
    pass

try:
    pass
except BaseException as be:
    # no warning here, all good
    pass

try:
    pass
except BaseException:
    # no warning here, all good
    pass


def func(**kwargs):
    try:
        is_debug = kwargs["debug"]
    except:
        # should be except KeyError:
        return


try:
    pass
except ():
    # Literal empty tuple is just like bare except:
    pass
