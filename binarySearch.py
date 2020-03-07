def binarySearch(result, left, right, t):

    if left > right:
        return None

    mid = (left + right) // 2

    if result[mid] == t:
        return mid

    if result[mid] > t:
        return binarySearch(result, left, mid-1, t)

    else:
        return binarySearch(result, mid+1, right, t)

if __name__=="__main__":

    result = [x for x in range(1, 10 + 1)]
    target = 7

    print(binarySearch(result, 0, len(result), target))