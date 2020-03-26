def selection_sort(data):

    for i in range(len(data) - 1):
        min = i

        for j in range(i, len(data)):
            if data[min] > data[j]:
                min = j

        data[i], data[min] = data[min], data[i]

    return data

if __name__=="__main__":
    data = [9, 4, 5, 6, 2, 3, 1, 8, 7, 10]

    data = selection_sort(data)

    print(data)