class LinearProbing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size

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
                return None

            if self.a[i] == key:
                self.d[i] = data
                return None

            j += 1
            i = (initial_position + j) % self.M

            if i == initial_position:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1

        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]

            i = (initial_position + j) % self.M
            j += 1

            if i == initial_position:
                return None

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

    t = LinearProbing(13)

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