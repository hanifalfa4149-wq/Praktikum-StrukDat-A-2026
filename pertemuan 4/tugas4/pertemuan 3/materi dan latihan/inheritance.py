class Animal:
    def __init__(self, nama):
        self.name = nama

    def panggil(self):
        print(f"halo {self.name}, bagaimana kabarmu")


class anjing(Animal):
    pass


d1 = anjing("Habib")
print()
d1.panggil()
print()
