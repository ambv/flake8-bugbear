"""
Should emit:
B901 - on lines 8, 35
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


async def not_broken4():
    import asyncio
    await asyncio.sleep(1)
    return 1


def actually_not_broken():
    yield 2
    return 1  # noqa


def not_broken5():
    def inner():
        return 2

    yield inner()
