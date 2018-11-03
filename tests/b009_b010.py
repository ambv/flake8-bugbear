"""
Should emit:
B009 - Line 15
B010 - Line 22
"""

# Valid getattr usage
getattr(foo, bar)
getattr(foo, "bar", None)
getattr(foo, "bar{foo}".format(foo="a"), None)
getattr(foo, "bar{foo}".format(foo="a"))
getattr(foo, bar, None)

# Invalid usage
getattr(foo, "bar")

# Valid setattr usage
setattr(foo, bar, None)
setattr(foo, "bar{foo}".format(foo="a"), None)

# Invalid usage
setattr(foo, "bar", None)
