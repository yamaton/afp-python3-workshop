# example from "Fluent Python"

# creation of a simple function registry


registry = []


def register(func):
    print("registering function {0}".format(func))
    registry.append(func)
    return func


def stacked(active=True):
    def decorate(func):
        if active:
            print("stacked function {0} is active".format(func))
        else:
            print("stacked function {0} is inactive".format(func))

        def decorated(*args,**kwargs):
            result = func(*args,*kwargs)
            return result
        return decorated
    return decorate


@stacked(active=True)
@register
def add(x, y):
    return x + y


@stacked(active=False)
@register
def mul(x, y):
    return x * y
