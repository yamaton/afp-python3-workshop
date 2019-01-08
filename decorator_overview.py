# example from "Fluent Python"


def register(func):
    print("registering function {0}".format(func))


@register
def add(x, y):
    return x + y


@register
def mul(x, y):
    return x * y
