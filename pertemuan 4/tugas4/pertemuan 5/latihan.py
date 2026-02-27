# Latihan 1
stock_barang = [15, 40, 30, 10, 25]

indekSepuluh = stock_barang.index(10)
stock_barang[indekSepuluh] = 50

stock_barang.append(5)
urut = sorted(stock_barang)
stock_barang_baru = list(reversed(urut))
print()
print(stock_barang_baru)
print()
rata_rata = sum(stock_barang_baru) / len(stock_barang_baru)
kata = "Stock aman" if rata_rata > 20 else "Stock kurang"
print(kata)
print()

# Latihan 2
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

for x in data_aktivitas:
    if x[1] > 80:
        print(x[0], "mendapatkan predikat gold")
    elif x[1] >= 50 and x[1] <= 80:
        print(x[0], "mendapatkan predikat silver")
    else:
        print(x[0], "mendapatkan predikat bronze")

print()
# Latihan 3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

print(ukm_coding - ukm_robotik)
print(set(ukm_coding | ukm_robotik))

if "Andi" in ukm_robotik:
    print("True")
else:
    print("False")

print()
# Latihan 4
gudang_pc = [
    {"item": "Monitor", "Harga": 1500000, "Stok": 5},
    {"item": "Keyboard", "harga": 400000, "Stok": 12},
    {"item": "Mouse", "harga": 250000, "Stok": 20},
]

gudang_pc[1].update({"kategori": "Aksesoris", "keyboard": "Mechanical"})
gudang_pc.append({"item": "Headset", "harga": 350000, "Stok": 8})
total_monitor = gudang_pc[0]["Harga"] * gudang_pc[0]["Stok"]
total_keyboard = gudang_pc[1]["harga"] * gudang_pc[1]["Stok"]
total_mouse = gudang_pc[2]["harga"] * gudang_pc[2]["Stok"]
total_headset = gudang_pc[3]["harga"] * gudang_pc[3]["Stok"]

print(f"Total harga Monitor: Rp{total_monitor}")
print(f"Total harga Keyboard: Rp{total_keyboard}")
print(f"Total harga mouse: Rp{total_mouse}")
print(f"Total harga headset: Rp{total_headset}")
