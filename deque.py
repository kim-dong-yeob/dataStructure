from collections import deque

dq= deque()

dq.append("A")
dq.appendleft("B")
dq.append("C")

for e in dq:
    print(e, end=' ')

print()
dq.pop()
dq.popleft()

for e in dq:
    print(e, end=' ')


