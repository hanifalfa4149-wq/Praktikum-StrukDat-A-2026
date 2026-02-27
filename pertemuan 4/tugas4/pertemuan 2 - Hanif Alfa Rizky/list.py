nilai = [75, 80, 65, 90, 85]

nilai.append(95)
nilai.remove(65)
nilai.sort()
print("Nilai tertinggi:", nilai[-1])
print("Nilai Terendah:", nilai[0])
print("Jumlah nilai:", len(nilai))
print("Rata-rata nilai:", sum(nilai) / len(nilai))
print(nilai)
