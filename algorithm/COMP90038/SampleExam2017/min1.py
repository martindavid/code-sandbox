def min1(arr):
    n = len(arr)
    print(arr)
    if n == 1:
        return arr[0]
    else:
        temp = min1(arr[0:n - 1])
        print(temp)
        if temp <= arr[n]:
            return temp
        else:
            return arr[n]

A = [8, 1, 3, 7, 5, 2, 12]
print(min1(A))
