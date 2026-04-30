# Nama   : Hanif Alfa Rizky
# NIM    : 25071104149
# Praktikum 11 - Struktur Data

# =============================================
# CLASS NODE
# Setiap pasien disimpan sebagai node
# =============================================
class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None  # pointer ke node berikutnya


# =============================================
# CLASS QUEUE (berbasis Linked List manual)
# =============================================
class AntrianRumahSakit:
    def __init__(self):
        self.head = None   # pasien paling depan
        self.tail = None   # pasien paling belakang
        self._size = 0     # counter jumlah pasien
        self._nomor_antrian = 0  # buat nomor urut daftar

    # --- Daftarkan pasien baru ke belakang antrian ---
    def enqueue(self, nama, keluhan):
        self._nomor_antrian += 1
        pasien_baru = Node(nama, keluhan)

        if self.tail is None:
            # antrian kosong, head dan tail sama-sama nunjuk node baru
            self.head = pasien_baru
            self.tail = pasien_baru
        else:
            # sambung node lama ke node baru
            self.tail.next = pasien_baru
            self.tail = pasien_baru

        self._size += 1
        print(f"[DAFTAR] {nama.capitalize()} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._nomor_antrian})")

    # --- Panggil dan keluarkan pasien paling depan ---
    def dequeue(self):
        if self.is_empty():
            print("[PANGGIL] Antrian kosong, tidak ada pasien yang bisa dipanggil.")
            return None

        pasien_dipanggil = self.head
        self.head = self.head.next  # geser head ke pasien berikutnya

        # kalau antrian jadi kosong, tail juga harus None
        if self.head is None:
            self.tail = None

        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {pasien_dipanggil.nama.upper()} (keluhan: {pasien_dipanggil.keluhan})")
        return pasien_dipanggil

    # --- Lihat pasien paling depan tanpa mengeluarkannya ---
    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong.")
            return None

        print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} — {self.head.keluhan}")
        return self.head

    # --- Cek apakah antrian kosong ---
    def is_empty(self):
        return self.head is None

    # --- Hitung jumlah pasien dalam antrian ---
    def size(self):
        return self._size

    # --- Kosongkan seluruh antrian ---
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    # --- Tampilkan semua pasien dalam antrian ---
    def tampilkan_antrian(self):
        if self.is_empty():
            print("[ANTRIAN SAAT INI] Antrian kosong.")
            return

        print("[ANTRIAN SAAT INI]")
        current = self.head
        nomor = 1
        while current is not None:
            print(f"  {nomor}. {current.nama.upper():<10} → {current.keluhan}")
            current = current.next
            nomor += 1


# =============================================
# PROGRAM UTAMA - Skenario Pagi Hari
# =============================================
def main():
    print("=" * 36)
    print("  SISTEM ANTRIAN POLI UMUM")
    print("  RS Sehat Bersama")
    print("=" * 36)
    print()

    antrian = AntrianRumahSakit()

    # 1. Cek antrian sebelum ada pasien
    if antrian.is_empty():
        print("[CEK] Apakah antrian kosong? → YA, antrian masih kosong.")
    else:
        print("[CEK] Apakah antrian kosong? → TIDAK, masih ada pasien.")
    print()

    # 2-4. Tiga pasien pertama daftar
    antrian.enqueue("Budi", "demam tinggi")
    antrian.enqueue("Ani", "batuk pilek")
    antrian.enqueue("Citra", "sakit kepala")
    print()

    # 5. Tampilkan jumlah pasien
    print(f"[INFO] Jumlah pasien menunggu: {antrian.size()} orang")

    # 6. Peek - cek siapa yang paling depan
    antrian.peek()
    print()

    # 7. Dokter panggil pasien pertama
    antrian.dequeue()

    # 8. Pasien Dodi daftar
    antrian.enqueue("Dodi", "nyeri perut")
    print()

    # 9. Tampilkan antrian saat ini
    antrian.tampilkan_antrian()
    print()

    # 10. Dokter panggil pasien berikutnya
    antrian.dequeue()

    # 11. Tampilkan sisa pasien
    print(f"[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")
    print()

    # 12. Sesi selesai, kosongkan antrian
    antrian.clear()

    # 13. Cek antrian setelah di-clear
    if antrian.is_empty():
        print("[CEK] Apakah antrian kosong? → YA, antrian sudah kosong.")
    else:
        print("[CEK] Apakah antrian kosong? → TIDAK, masih ada pasien.")

    print()
    print("=" * 36)
    print("  Simulasi Selesai!")
    print("=" * 36)


if __name__ == "__main__":
    main()