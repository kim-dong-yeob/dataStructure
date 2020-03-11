class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class Bst:
    def __init__(self):
        self.root = None

    def get(self, k):
        return self.get_item(self.root, k)

    def get_item(self, n, k):
        if n == None:
            return None
        if n.key > k:
            return self.get_item(n.left, k)
        elif n.key < k:
            return self.get_item(n.right, k)
        else:
            return n.value

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value

        return n

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def delete_min(self):
        if self.root == None:
            print("tree is empty")
        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n

    def delete(self, k):
        self.root = self.del_node(self.root, k)

    def del_node(self, n, k):
        if n == None:
            return None
        if n.key > k:
            n.left = self.del_node(n.left, k)
        elif n.key < k:
            n.right = self.del_min(n.right, k)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            tg = n
            n = self.minimum(tg.right)
            n.right = self.del_min(tg.right)
            n.left = tg.left
        return n

    def preorder(self, n):
        if n != None:
            print(str(n.key), '  ', end=' ')

            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        if n != None:

            if n.left:
                self.inorder(n.left)

            print(str(n.key), '  ', end=' ')

            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        if n != None:

            if n.left:
                self.postorder(n.left)

            if n.right:
                self.postorder(n.right)

            print(str(n.key), '  ', end=' ')

if __name__=="__main__":
    t = Bst()
    t.put(500, "A")
    t.put(600, "B")
    t.put(200, "E")
    t.put(100, "D")
    t.put(400, "C")
    t.put(250, "H")
    t.put(150, "F")
    t.put(800, "G")
    t.put(700, "I")
    t.put(50, "J")
    t.put(350, "K")
    t.put(10, "L")
    t.preorder(t.root)
    print()
    t.inorder(t.root)
    print()
    t.postorder(t.root)
    print()

