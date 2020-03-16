class QuadProbing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
        self.N = 0

    def hash(self, key):
        return key % self.M

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0

        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1

                return

            if self.a[i] == key:
                self.d[i] = data

                return

            j += 1
            i = (initial_position + j * j) % self.M

            if self.N > self.M:
                break


    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1

        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]

            i = (initial_position + j * j) % self.M
            j += 1

        return None

    def print_table(self):
        for i in range(self.M):
            print("{:4}".format(str(i)), end=' ')

        print()

        for i in range(self.M):
            print("{:4}".format(str(self.a[i])), end=' ')

        print()

        for i in range(self.M):
            print("{:4}".format(str(self.d[i])), end=' ')

        print()

if __name__=="__main__":

    t = QuadProbing(13)

    t.put(25, "A")
    t.put(37, "B")
    t.put(18, "C")
    t.put(55, "D")
    t.put(22, "E")
    t.put(35, "F")
    t.put(50, "G")
    t.put(63, "H")
    t.put(69, "I")
    print(t.print_table())

    print(t.get(69))
