import heapq

data = [9, 4, 5, 6, 2, 3, 1, 8, 7, 10]

heapq.heapify(data)
print("minimum heap:\t", data)

r = []

while data:
    r.append(heapq.heappop(data))

print("result:\t", r)