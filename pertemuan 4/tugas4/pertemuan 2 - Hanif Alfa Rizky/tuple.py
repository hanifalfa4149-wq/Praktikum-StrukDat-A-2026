dosen = ("D001", "Dr.Andi", "Struktur Data", 12)

print("nama dosenn", dosen[1])
print("mata kuliah", dosen[2])
for x in dosen:
    print(x)
dosen.append(3, 14)  # 'tuple' object has no attribute 'append'
# tuple itu immutable, jadi lebih aman dari list yang terlalu fleksibel
