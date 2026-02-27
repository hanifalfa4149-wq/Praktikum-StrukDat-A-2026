mahasiswa = {
    "M001": {"nama": "Ali", "prodi": "Informatika", "IPK": 3.60},
    "M002": {"nama": "Doni", "prodi": "Sistem Informasi", "IPK": 3.25},
    "M003": {"nama": "Citra", "prodi": "Informatika", "IPK": 3.80},
}
for x in mahasiswa:
    if mahasiswa[x]["IPK"] >= 3.5:
        print(f"{mahasiswa[x]["nama"]}")

rata_rata_IPK = sum(mahasiswa[x]["IPK"] for x in mahasiswa) / len(mahasiswa)
print(f"Rata-rata IPK mahasiswa: {rata_rata_IPK:.2f}")
mahasiswa.update(
    {"M004": {"nama": "habib", "prodi": "Teknik Informatika", "IPK": 2.30}}
)
print(mahasiswa)
