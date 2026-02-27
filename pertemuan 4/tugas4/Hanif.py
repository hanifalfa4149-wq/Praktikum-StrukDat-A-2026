# PYTHON OUTPUT

print("syikbi ganteng")
print("syikbi umurnya", 20, "tahun")

# PYTHON COMMENT <<<< INI COMMENT NANAMNYA NI
"""
gini bisa juga kalau
line nya banyak
"""

# PYTHON VARIBEL NAMING

# yang boleh
syikbiganteng = "gacor"
syikbi_ganteng = "gacor"
_syikbi_ganteng = "gacor"
syikbiGanteng = "gacor"
SYIKBI = "gacor"
syikbi9 = "gacor"

# yang tidak boleh
9syikbi = "gacor"
syikbi-ganteng = "gacor"
syikbi ganteng = "gacor"

# ada 3 tipe naming standar
syikbiGanteng = "gacor" # camel case
SyikbiGanteng = "gacor" # Pascal case
syikbi_ganteng = "gacor" #snake case >>> ini standar python

# PYTHON DATA TYPES

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

# contoh
nama = "syikbi"          # str
umur = 20                 # int
tinggi = 170.5            # float
is_ganteng = True        # bool
hobi = ["makan", "tidur"] # list
data_diri = {"nama": "syikbi", "umur": 20} # dict
nilai = None              # NoneType
angka_complex = 3 + 5j   # complex
range_angka = range(1, 10) # range

# PYTHON NUMBER

A = 9999    # int
B = 99.99  # float
C = 3 + 5j   # complex

# PYTHON CASTING

A = str(99.99)    # A nya jadi "99.99"
B = int(99.99)    # B akan menjadi 99
C = float(99.99)  # C akan menjadi 99.99

# PYTHON STRING

A = "Syikbi Ganteng"

# Slicing
print(A[0:4])   # "Syik" (index 0 sampai sebelum 4)
print(A[:4])    # "Syik" (dari awal sampai sebelum 4)
print(A[5:])    # "Ganteng" (dari index 5 sampai akhir)
print(A[::-1])  # "gnetnaG ibkiyS" (dibalik/reverse)

# Gabung & Kali
print("syikbi" + "ganteng") # "syikbiganteng"
print("Gacor" * 3)     # "GacorGacorGacor"

# PYTHON BOOLEAN

# 1. Nilai Dasar cuma 2 ni
A = True
B = False

# operasi
print(10 == 10)  # True (Sama dengan)
print(10 != 5)   # True (Tidak sama dengan)
print(10 > 15)   # False (Lebih besar)
print(5 <= 5)    # True (Kurang dari sama dengan)

# operator logika
A = True
B = False

print(A and B)   # False (Dua-duanya harus True)
print(A or B)    # True (Salah satu True aja udah cukup)
print(not A)     # False (Kebalikan/Negasi)

# Fungsi bool()
# Semua yang di bawah ini hasilnya FALSE
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))

# Semua yang di bawah ini hasilnya TRUE
print(bool("Syikbi")) # String ada isinya
print(bool(100))   # Angka bukan nol
print(bool(["Syikbi", "Ganteng"])) # List ada isinya

# Contoh Penggunaan di If-Else
syikbi_ganteng = True

if syikbi_ganteng:
    print("Syikbi ganteng banget!")
else:
    print("Dak mungkin else, syikbi pasti ganteng")