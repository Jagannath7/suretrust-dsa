

# N stairs


def stairs(n, k):

    if n == 0:
        return 1
    if n<0:
        return 0

    return stairs(n-3, k) + stairs(n-2, k) + stairs(n-1, k)


def KstepsAtaTime(n, k):

    if n == 0:
        return 1

    if n<0:
        return 0
    ans = 0
    for i in range(1, k+1):
        ans += KstepsAtaTime(n-i, k)

    return ans
# print(KstepsAtaTime(5, 3))

def tiles(n):

    #Base case

    if n<4:
        return 1

    # Recursive case

    return tiles(n-1) + tiles(n-4)


def binary_search(arr, l, r, key):

    if l>r:
        return -1

    mid = (l+r)//2

    if arr[mid] == key:
        return mid

    elif arr[mid] > key:
        return binary_search(arr, l, mid - 1, key)

    else:
        return binary_search(arr, mid+1, r, key)



def binary_strings(n, last_digit):

    # base case

    if n == 0:
        return 0

    if n == 1:
        if last_digit == 0:
            return 2
        else:
            return 1

    if last_digit == 0:
        return binary_strings(n-1, 0) + binary_strings(n-1, 1)
    else:
        return binary_strings(n-1, 0)


# print(binary_strings(3, 0))


def friends_pairing(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return friends_pairing(n-1) + (n-1)*friends_pairing(n-2)


