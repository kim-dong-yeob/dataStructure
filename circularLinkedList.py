class CLL:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def sizeCheck(self):
        return self.size

    def insert(self, item):
        n = self.Node(item, None)
        if self.empty():
            n.next = n
            self.last = n

        else:
            n.next = self.last.next
            self.last.next = n
            
        self.size += 1

    def first(self):
        if self.empty():
            return "underFlow"

        f = self.last.next
        return f.item

    def delete(self):
        if self.empty():
            return "underFlow"

        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next
            
        self.size -= 1

    def print_list(self):
        if self.empty():
            return "underFlow"
        else:
            f = self.last.next
            p = f

            while p.next != f:
                print(p.item, ' -> ', end=' ')
                p = p.next
            print(p.item)

if __name__=="__main__":

    s = CLL()
    s.insert("A")
    s.insert("B")
    s.insert("C")
    s.insert("D")
    s.print_list()
    print(s.sizeCheck())
    s.delete()
    s.print_list()
    print(s.sizeCheck())
