def push(item):
    s.append(item)

def pop():
    if len(s) != 0:
        item = s.pop()
        return item

def peek():
    if len(s) != 0:
        return s[-1]

s = []

push("A")
push("B")
push("C")

print(s)

pop()

print(s)
print(peek())
