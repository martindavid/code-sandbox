def find_number_keys(Arr, k):
    n = len(Arr)
    result = 0
    for i in range(n):
        if (Arr[i] <= k):
            print(i)
            result += 1
    return result


def find_number_keys_recursive(Arr, lo, hi, k):
    print('lo: %d, hi: %d' %(lo, hi))
    if abs(Arr[lo]) <= k and abs(Arr[hi]) <= k:
        return (hi - lo) + 1
    if abs(Arr[lo]) > k and abs(Arr[hi]) <= k:
        return find_number_keys_recursive(Arr, lo + 1, hi, k)
    else:
        return find_number_keys_recursive(Arr, lo, hi - 1, k)

Arr = [-10 ,-5, -1, 0, 3, 6, 7,  9]
#print('Result: %d' % find_number_keys(Arr, 4))
n = len(Arr)
keys = find_number_keys_recursive(Arr, 0,  n - 1, 8)
print('Result %d' % keys)