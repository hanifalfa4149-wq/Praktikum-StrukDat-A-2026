from tabulate import tabulate
import kurs
import konverter

print("=== KONVERTER MATA UANG ===")

data_untuk_tabel = []
for k in kurs.data_kurs:
    nilai = kurs.data_kurs[k]
    data_untuk_tabel.append([k, nilai])

headers = ["Kode", "Kurs"]
print(tabulate(data_untuk_tabel, headers=headers, tablefmt="grid"))
print()

dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke   (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

rupiah_sementara = konverter.ke_idr(dari, jumlah)
hasil_akhir = konverter.dari_idr(ke, rupiah_sementara)

print("\nHasil Konversi:")
print(f"{jumlah} {dari} = {hasil_akhir:.2f} {ke}")
