katalog = [
    {"nama": "Belajar Python", "harga": 75000, "stok": 5},
    {"nama": "Struktur Data", "harga": 95000, "stok": 3},
    {"nama": "Algoritma Dasar", "harga": 60000, "stok": 8},
]


def cari_buku(keywords):
    keywords = keywords.lower()

    hasil = []

    for buku in katalog:
        if keywords in buku["nama"].lower():
            hasil.append(buku)
    return hasil


masukan = input("Masukkan judul buku yang ingin dicari: ")
cari = cari_buku(masukan)

print()
if cari:
    print("Buku yang ditemukan:")
    for buku in cari:
        print(f"Nama: {buku['nama']}, Harga: {buku['harga']}, Stok: {buku['stok']}")
else:
    print("Buku tidak ditemukan.")
print()
