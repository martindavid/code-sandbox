from __future__ import print_function


def search(arr, lo, hi):
    "Search the first occurence of value 1"
    m = (lo + hi) / 2
    if arr[m] == 1 and arr[m - 1] == 0:
        return m
    elif arr[m + 1] == 1:
        return m + 1

    if arr[m + 1] == 0:
        return search(arr, m + 1, hi)
    else:
        return search(arr, lo, m - 1)


ARR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
print(search(ARR, 0, len(ARR) - 1))
