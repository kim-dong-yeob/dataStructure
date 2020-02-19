
class SLL:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)

        self.size += 1

    def delete_front(self):
        if self.empty():
            return "underFlow"
        else:
            self.head = self.head.next

    def print(self):
        p = self.head

        while p:
            if p.next != None:
                print(p.item + ' -> ', end=' ')
            else:
                print(p.item)

            p = p.next

if __name__ == "__main__":
    s = SLL()
    s.insert_front("A")
    s.delete_front()
    s.print()
