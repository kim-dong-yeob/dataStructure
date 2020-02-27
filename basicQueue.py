def add(item):
    q.append(item)

def remove():
    if len(q) != 0:
        item = q.pop(0)
        return item

def print_q():
    print('front -> ', end='  ')

    for i in range(len(q)):
        print(q[i], end='  ')
    print('  <- rear')

q = []

add('A')
add('B')
add('C')

print_q()

remove()

print_q()
