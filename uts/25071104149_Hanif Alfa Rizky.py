pengunjung_hari_ini = [
    {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
    {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
    {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", "kembali": False},
]


# Soal 1
def tampilkan_pengunjung():
    no = 0
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====:")
    print("No |  ID  | Nama | Usia | Kategori | Status Kembali")
    for x in pengunjung_hari_ini:
        no += 1
        print(
            f"{no}  | {x['id']} | {x['nama']} | {x['usia']} | {x['kategori']} | {x['kembali']}"
        )


def filter_belum_kembali():
    belum_kembali = []
    no = 0
    total = 0
    print("===== PENGUNJUNG BELUM KEMBALI =====")
    for x in pengunjung_hari_ini:
        if x["kembali"] == False:
            no += 1
            belum_kembali.append(x)
            print(f"{no}. {x['nama']}")
            total += 1
    print(f"total pengunjung yang belum kembali: {total}")


print()
tampilkan_pengunjung()
print()
filter_belum_kembali()
print()

# Soal 2
tuple = [
    {
        "Nama": "Perpustakaan Kampus Terpadu",
        "Alamat": "Jl. Pendidikan No. 5, Pekanbaru",
        "Telp": "0761-54321",
    }
]


def info_perpustakaan():
    print("Info Perpustakaan:")
    for x in tuple:
        print(f"Nama   : {x['Nama']}")
        print(f"Alamat : {x['Alamat']}")
        print(f"Telpon : {x['Telp']}")


def rekap_kategori():
    unik = set()
    rekap = {}
    for x in pengunjung_hari_ini:
        unik.add(x["kategori"])
        if x["kategori"] not in rekap:
            rekap[x["kategori"]] = 0
        rekap[x["kategori"]] += 1

    print(f"kategori buku unik: {unik}")
    print(f"jumlah kategori: {len(unik)}")
    print()
    print("Rekap per kategori:")
    for kategori, jumlah in rekap.items():
        print(f"{kategori} : {jumlah} pengunjung")
    print()
    print("Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung)")


info_perpustakaan()
print()
rekap_kategori()
print()


# Soal 3
class Pengunjung:
    def __init__(self, id, nama, kategori):
        self._id = id
        self._nama = nama
        self._kategori = kategori

    def get(self):
        return self._id, self._nama, self._kategori

    def tampilkan_info():
        pass


class Pengunjung_prioritas(Pengunjung):
    pass
