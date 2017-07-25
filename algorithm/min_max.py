def find_min_max(arr):
    n = len(arr)
    if n == 0:
        return -1

    min = arr[0]
    max = arr[0]
    for i in range(n - 1):
        if arr[i] > max:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]
    return min, max

A = [10, 29, 5, 12, 30, 45]
min, max = find_min_max(A)
print(min, max)
