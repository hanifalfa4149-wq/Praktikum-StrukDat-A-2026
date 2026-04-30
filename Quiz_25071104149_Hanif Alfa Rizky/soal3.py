katalog = [
    {"nama": "Belajar Python", "harga": 75000, "stok": 5},
    {"nama": "Struktur Data", "harga": 95000, "stok": 3},
    {"nama": "Algoritma Dasar", "harga": 60000, "stok": 8},
]


def proses_transaksi(katalog, nama_buku, jumlah_beli):
    for buku in katalog:
        if buku["nama"] == nama_buku:
            if buku["stok"] >= jumlah_beli:
                total_harga = buku["harga"] * jumlah_beli
                buku["stok"] -= jumlah_beli
                return total_harga
            else:
                return "Stok tidak cukup"
    return "Buku tidak ditemukan"


nama_buku = input("Masukkan nama buku yang ingin dibeli: ")
jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))
total = proses_transaksi(katalog, nama_buku, jumlah_beli)

riwayat_transaksi = set()
riwayat_transaksi.add(total)
print(f"Total harga: {total}")
print(f"Riwayat transaksi: {riwayat_transaksi}")
