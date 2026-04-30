def tambah_buku(nama, harga, stok):
    return nama, harga, stok


nama_buku = str(input("masukkan nama buku: "))
harga_buku = int(input("masukkan harga buku: "))
stok_buku = int(input("masukkan stok buku: "))

nambah_buku = tambah_buku(nama_buku, harga_buku, stok_buku)

total_buku = {
    "nama": nama_buku,
    "harga": harga_buku,
    "stok": stok_buku,
}

if harga_buku > 0 and stok_buku > 0:
    total = []

    total.append(total_buku)
    print(total)
else:
    print("[ERROR]")
