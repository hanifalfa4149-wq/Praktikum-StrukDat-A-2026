class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        sekarang = self.root
        while True:
            if value < sekarang.value:
                if sekarang.left is None:
                    sekarang.left = Node(value)
                    return
                sekarang = sekarang.left
            else:
                if sekarang.right is None:
                    sekarang.right = Node(value)
                    return
                sekarang = sekarang.right

    def pre_order(self, node, hasil):
        if node is None:
            return
        hasil.append(node.value)
        self.pre_order(node.left, hasil)
        self.pre_order(node.right, hasil)

    def in_order(self, node, hasil):
        if node is None:
            return
        self.in_order(node.left, hasil)
        hasil.append(node.value)
        self.in_order(node.right, hasil)

    def post_order(self, node, hasil):
        if node is None:
            return
        self.post_order(node.left, hasil)
        self.post_order(node.right, hasil)
        hasil.append(node.value)


def main():
    data = ["F", "B", "G", "A", "D", "C", "E", "I", "H"]
    bst = BinarySearchTree()
    for i in data:
        bst.insert(i)

    sebelum = []
    di = []
    setelah = []

    bst.pre_order(bst.root, sebelum)
    bst.in_order(bst.root, di)
    bst.post_order(bst.root, setelah)

    print()
    print("Pre-order :", " ".join(sebelum))
    print("In-order  :", " ".join(di))
    print("Post-order:", " ".join(setelah))
    print()


if __name__ == "__main__":
    main()
