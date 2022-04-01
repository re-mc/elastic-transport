class MyClass:
    def __init__(self, name, message):
        print(f'[{name}]: {message}')
        self.name = name
        self.message = message
    def say(self, message):
        print(f'[{self.name}]: {message}')
    def sayAgain(self):
        print(f'[{self.name}]: {self.message}')