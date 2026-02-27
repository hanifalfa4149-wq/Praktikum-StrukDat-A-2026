class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("chirp")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("meow")


b1 = Bird()
c2 = Cat()

for x in (b1, c2):
    x.sound()
