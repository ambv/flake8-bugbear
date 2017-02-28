class NoWarningsMoreMethods:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def other_function(self):
        ...


class NoWarningsClassAttributes:
    spam = 'ham'

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


class NoWarningsComplicatedAssignment:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar
        self.spam = ' - '.join([foo, bar])


class NoWarningsMoreStatements:
    def __init__(self, foo, bar):
        foo = ' - '.join([foo, bar])
        self.foo = foo
        self.bar = bar


class Warnings:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar
