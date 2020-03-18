class DoubleHashing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
        self.N = 0

    def hash(self, key):
        return key % self.M

    def dKey(self, key):
        return self.M // 2 + 1 - (key % (self.M // 2 + 1))

    def extendedHash(self, key, j):
        return (self.hash(key) + j * (self.dKey(key))) % self.M

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 1

        if self.a[i] == None:
            self.a[i] = key
            self.d[i] = data
            self.N += 1

            return

        while True:
            i = self.extendedHash(key, j)

            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1

                return

            j += 1

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

    t = DoubleHashing(13)

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
