def find_number_keys(Arr, k):
    n = len(Arr)
    result = 0
    for i in range(n):
        if (Arr[i] <= k):
            print(i)
            result += 1
    return result

Arr = [-5, -1, 0, 3, 6, 9]
print('Result: %d' % find_number_keys(Arr, 4))