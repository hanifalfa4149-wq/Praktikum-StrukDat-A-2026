class NodeAntri:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class AntrianKasir:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        antrian_baru = NodeAntri(nama)
        if not self.head:
            self.head = antrian_baru
            antrian_baru.next = self.head
        else:
            cek = self.head
            while cek.next != self.head:
                cek = cek.next
            cek.next = antrian_baru
            antrian_baru.next = self.head

    def print_antrian(self):
        if not self.head:
            return
        cek = self.head
        while True:
            print(cek.nama, end=" -> ")
            cek = cek.next
            if cek == self.head:
                break
        print("(kembali ke", self.head.nama + ")")

    def delete_head(self):
        if not self.head:
            return

        if self.head.next == self.head:
            self.head = None
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head


print()
antrian = AntrianKasir()
for orang in ["Andi", "Budi", "Citra", "Dina"]:
    antrian.insert_tail(orang)

antrian.print_antrian()

antrian.insert_tail("Edo")
antrian.print_antrian()

antrian.delete_head()
antrian.print_antrian()
print()
