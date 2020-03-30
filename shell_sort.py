def shell_sort(data):
    h = 4
    while h >= 1:
        for i in range(h, len(data)):
            j = i

            while j >= h and data[j] < data[j - h]:
                data[j], data[j - h] = data[j - h], data[j]
                j -= h

        h //= 3

    return data

if __name__=="__main__":
    data = [9, 4, 5, 6, 2, 3, 1, 8, 7, 10]

    data = shell_sort(data)

    print(data)