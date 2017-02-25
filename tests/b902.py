def not_a_method(arg1):
    ...


class NoWarnings:
    def __init__(self):
        def not_a_method_either(arg1):
            ...

    def __new__(cls, *args, **kwargs):
        ...

    def method(self, arg1, *, yeah):
        ...

    @classmethod
    def someclassmethod(cls, arg1, with_default=None):
        ...

    @staticmethod
    def not_a_problem(arg1):
        ...


class Warnings:
    def __init__(i_am_special):
        ...

    def almost_a_class_method(cls, arg1):
        ...

    def almost_a_static_method():
        ...

    @classmethod
    def wat(self, i_like_confusing_people):
        ...

    def i_am_strange(*args, **kwargs):
        self = args[0]

    def defaults_anyone(self=None):
        ...

    def invalid_kwargs_only(**kwargs):
        ...

    def invalid_keyword_only(*, self):
        ...


class Meta(type):
    def __init__(cls, name, bases, d):
        ...


class OtherMeta(type):
    def __init__(self, name, bases, d):
        ...
