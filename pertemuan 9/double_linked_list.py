class NodeBuku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.next = None
        self.prev = None


class DataBuku:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_tail(self, judul, penulis):
        buku_baru = NodeBuku(judul, penulis)
        if self.head is None:
            self.head = self.tail = buku_baru
        else:
            buku_baru.prev = self.tail
            self.tail.next = buku_baru
            self.tail = buku_baru

    def print_forward(self):
        buku_skrg = self.head
        while buku_skrg:
            print(f"{buku_skrg.judul} ({buku_skrg.penulis})", end=" <-> ")
            buku_skrg = buku_skrg.next
        print("Selesai")

    def print_backward(self):
        buku_skrg = self.tail
        while buku_skrg:
            print(f"{buku_skrg.judul} ({buku_skrg.penulis})", end=" <-> ")
            buku_skrg = buku_skrg.prev
        print("Selesai")

    def delete_by_judul(self, target):
        buku_skrg = self.head
        while buku_skrg:
            if buku_skrg.judul == target:
                if buku_skrg.prev:
                    buku_skrg.prev.next = buku_skrg.next
                else:
                    self.head = buku_skrg.next
                if buku_skrg.next:
                    buku_skrg.next.prev = buku_skrg.prev
                else:
                    self.tail = buku_skrg.prev
                return
            buku_skrg = buku_skrg.next


print()
buku = DataBuku()
buku.insert_tail("Laskar Pelangi", "Andrea Hirata")
buku.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
buku.insert_tail("Sang Pemimpi", "Andrea Hirata")

buku.print_forward()
print()
buku.print_backward()
print()

buku.delete_by_judul("Bumi Manusia")
buku.print_forward()
print()
