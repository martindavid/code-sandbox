def InsertionSort(Arr):
    length = len(Arr)
    i = 1
    for i in range(length):
        v = Arr[i]
        j = i - 1
        while (j >= 0 and v < Arr[j]):
            Arr[j + 1] = Arr[j]
            j -= 1
        Arr[j + 1] = v
    return Arr 

Arr = [10,8,3,5,11,2,7]
print InsertionSort(Arr)
