class Mahasiswa:
    def __init__(self, nama, umur, status):
        self.nama = nama
        self.umur = umur
        self.status = status

    def sapa(self):
        print(f"haloo {self.nama}, apa kabar")

    def pacar(self):
        print(f"{self.nama} sekarang {self.status}")

    def age(self):
        if self.umur <= 18:
            print(f"{self.nama} masih kecil")
        else:
            print(f"{self.nama} sudah besar")


mahasiswa1 = Mahasiswa("Habib", 20, "masih single")
mahasiswa2 = Mahasiswa("ferdy", 18, "sudah taken")

mahasiswa1.sapa()
mahasiswa2.sapa()

print()

mahasiswa1.pacar()
mahasiswa2.pacar()

print()

mahasiswa1.age()
mahasiswa2.age()
