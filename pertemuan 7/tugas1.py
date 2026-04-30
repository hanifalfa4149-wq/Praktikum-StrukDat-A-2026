def pisahkan_kendaran(plat_nomor):
    ganjil = []
    genap = []

    for plat in plat_nomor:
        angka_terakhir = int(plat.split()[-1][-1])
        if angka_terakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)

    return ganjil, genap


plat_nomor = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
ganjil, genap = pisahkan_kendaran(plat_nomor)
print("Kendaraan Ganjil:", ganjil)
print("Kendaraan genap:", genap)
