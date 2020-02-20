
class DLL:
    class Node:
        def __init__(self, item, prev, link):
             self.item = item
             self.prev = prev
             self.next = link

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n

        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p, t)
        t.prev = n
        p.next = n
        self.size += 1

    def delete(self, p):
        t = p.next
        d = p.next
        t.next = d
        d.prev = t
        self.size -= 1

    def print_list(self):
        if self.empty():
            return "underFlow"
        else:
            p = self.head.next

            while p != self.tail:
                if p.next != self.tail:
                    print(p.item + ' < = > ', end=' ')
                else:
                    print(p.item)
                p = p.next

if __name__=="__main__":
    d = DLL()

    d.insert_after(d.head, 'A')
    d.insert_before(d.tail, 'B')
    d.insert_before(d.tail, 'C')
    d.insert_before(d.tail, 'D')
    d.insert_after(d.head.next, 'E')
    d.print_list()
