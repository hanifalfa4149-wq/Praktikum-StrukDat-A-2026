class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def panggil(self):
        print(f"Halo {self.name}, adakah seratus")


class Karyawan(Person):
    def __init__(self, Gaji):
        self._gaji = Gaji

    def get_gaji(self):
        return self._gaji

    def set_gaji(self, Gaji):
        if Gaji < 0:
            print("masak gaji minus")
        else:
            self._gaji = Gaji


class Rekening:
    def __init__(self, no_rekening, Pin):
        self.no_rekening = no_rekening
        self.__pin = Pin

    def set_Pin(self, Pin):
        if len(Pin) == 6:
            return self.__pin
        else:
            print("Pin harus 6 digit")


manusia = Person("Habib", "Laki-laki", 18)
manusia.panggil()

sales = Karyawan(3500000)
print(sales.get_gaji())

dana_kip = Rekening(123654, "666")
dana_kip.set_Pin("123456")
