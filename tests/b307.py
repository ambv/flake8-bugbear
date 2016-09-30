"""
Should emit:
B307 - on lines 6 and 34
"""

def broken():
    if True:
        return [1, 2, 3]

    yield 3
    yield 2
    yield 1


def not_broken():
    if True:
        return

    yield 3
    yield 2
    yield 1


def not_broken2():
    return not_broken()


def not_broken3():
    return

    yield from not_broken()


def broken2():
    return [3, 2, 1]

    yield from not_broken()
