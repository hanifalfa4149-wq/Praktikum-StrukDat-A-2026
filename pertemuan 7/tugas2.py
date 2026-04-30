class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambahKendaraan(self, plat):
        new_node = Node(plat)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def hapusKendaraan(self, plat):
        if self.head is None:
            return

        if self.head.plat == plat:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.plat == plat:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.plat, end=" -> ")
            current = current.next
        print("None")


kendaraan = LinkedList()
kendaraan.tambahKendaraan("B001")
kendaraan.tambahKendaraan("B002")
kendaraan.tambahKendaraan("B003")
kendaraan.tambahKendaraan("B004")
kendaraan.display()
kendaraan.hapusKendaraan("B002")
kendaraan.display()
