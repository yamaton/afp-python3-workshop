# Callable examples

# Let's say you wanted to create a greeter object for different situations
# One way to do this is to create a class called Greeter that keeps track
# of the greeting that it'll use to greet people.


class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        print(f"{self.greeting} {name}!")


# now we create different greeters

spanish_greeting = Greeter("hola")
spanish_greeting("Ram")

# the following is equivalent to the above example


def create_greeter(greeting):
    return lambda x: print(f"{greeting} {x}")


french_greeting = create_greeter("bonjour")
french_greeting("Ram")
