

def merge(arr, start, end):
    mid = (start + end)//2
    i = start
    j = mid + 1
    k = start

    temp = [-1] * 100

    while i<=mid and j <= end:

        if arr[j] < arr[i]:
            temp[k] = arr[j]
            j += 1

        else:
            temp[k] = arr[i]
            i += 1

        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j<=end:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(start, end+1):
        arr[i] = temp[i]


def merge_sort(arr, start, end):

    if start>=end:
        return

    mid = (start + end)//2

    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, end)

arr = [38, 27, 43, 3, 9, 82, 10]

merge_sort(arr, 0, len(arr)-1)

print(arr)
