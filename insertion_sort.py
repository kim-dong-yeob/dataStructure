def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j - 1] > data[j]:
                data[j], data[j - 1] = data[j - 1], data[j]

    return data

if __name__=="__main__":
    data = [9, 4, 5, 6, 2, 3, 1, 8, 7, 10]

    data = insertion_sort(data)

    print(data)