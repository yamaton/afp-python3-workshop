# Callable examples


class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        print(f"{self.greeting} {name}!")


spanish_greeting = Greeter("hola")
spanish_greeting("Ram")
