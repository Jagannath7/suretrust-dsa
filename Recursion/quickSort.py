arr = [12, 4, 78, 7, 23, 1, 45, 3, 90, 56]


def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    # put pivot in its right spot
    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    return i + 1


def quicksort(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)
    print(arr)
    quicksort(arr, start, p - 1)
    quicksort(arr, p + 1, end)


# quicksort(arr, 0, len(arr) - 1)
# print(arr)


def quickselect(arr, k):
    k = len(arr) - k

    start, end = 0, len(arr) - 1

    while start < end:
        p = partition(arr, start, end)

        if p < k:
            start = p + 1

        elif p > k:
            end = p - 1

        else:
            break

    return arr[p]


def kthSmallest(arr, start, end, k):

    if start <end:

        p = partition(arr, start, end)


        if p == k:
            return arr[p]

        elif p > k:
            return kthSmallest(arr, start, p-1, k)

        else:
            return kthSmallest(arr, p+1, end, k)


    return arr[start]

