KEAHLIAN_A = {"Python", "Java", "SQL", "Git"}
KEAHLIAN_B = {"Python", "C++", "Git", "Docker"}

keahlian_berdua = KEAHLIAN_A & KEAHLIAN_B
print("Keahlian yang dimiliki kedua mahasiswa:", keahlian_berdua)
hanya_keahlian_A = KEAHLIAN_A - KEAHLIAN_B
print("Keahlian yang hanya dimiliki mahasiswa A:", hanya_keahlian_A)
keahlian_unik = KEAHLIAN_A | KEAHLIAN_B
print("Semua keahlian unik yang dimiliki kedua mahasiswa:", keahlian_unik)
if "Java" in KEAHLIAN_B:
    print("Mahasiswa B memiliki keahlian Java")
