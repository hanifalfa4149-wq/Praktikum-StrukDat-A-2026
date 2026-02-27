# 1. PARENT CLASS (Induk) - Blueprint Umum
class Menu:
    def __init__(self, nama, harga):
        # ATRIBUT (Tempat nyimpen VALUE)
        self.nama = nama
        self.harga = harga

    # METHOD (Perilaku umum)
    def deskripsi(self):
        print(f"{self.nama} harganya Rp{self.harga}")

# 2. CHILD CLASS (Anak) - Lebih Spesifik (Inheritance)
class Makanan(Menu):
    def __init__(self, nama, harga, tingkat_pedas):
        # Ambil atribut dari Induk pake super()
        super().__init__(nama, harga)
        # Atribut tambahan khusus Makanan
        self.tingkat_pedas = tingkat_pedas

    # Method khusus makanan
    def deskripsi(self):
        print(f"Makanan: {self.nama} | Pedas: Level {self.tingkat_pedas} | Rp{self.harga}")

class Minuman(Menu):
    def __init__(self, nama, harga, suhu):
        super().__init__(nama, harga)
        self.suhu = suhu # Misal: "Dingin" atau "Panas"

    def deskripsi(self):
        print(f"Minuman: {self.nama} ({self.suhu}) | Rp{self.harga}")

# 3. OBJECT (Instance) - Menu yang beneran ada di meja
menu1 = Makanan("Nasi Goreng", 25000, 5) # Value: "Nasi Goreng", 25000, 5
menu2 = Minuman("Es Teh Manis", 5000, "Dingin")

# 4. EKSEKUSI
menu1.deskripsi() # Output: Makanan: Nasi Goreng | Pedas: Level 5 | Rp25000
menu2.deskripsi() # Output: Minuman: Es Teh Manis (Dingin) | Rp5000