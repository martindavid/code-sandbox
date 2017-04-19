def getMinimumUniqueSum(arr):
    n = len(arr)
    arr = sorted(arr)
    unique = list(set(arr))
    i = 0
    if len(arr) != len(unique):
        while len(arr) != len(unique):
            temp = arr[i]
            print(temp)
            for j, item in enumerate(unique):
                if temp == item:
                    temp = temp + 1
            # if temp != x:
            arr[i] = temp
            unique.append(temp)
            unique = sorted(unique)
            arr = sorted(arr)
            print(unique)
            i = i + 1
    sum = 0

    for i in range(n):
        sum = sum + unique[i]
    return sum


#print(getMinimumUniqueSum([3, 2, 1, 2, 7, 2, 2, 2, 2]))
print(getMinimumUniqueSum([2,2,2,2,2,2,2,2,2,2,2]))
#print(getMinimumUniqueSum([2,2,2,2,2,2,2,2,2,2,2,1]))
#print(getMinimumUniqueSum([3,2,1,2,7]))
#print(getMinimumUniqueSum([2, 2, 2, 4, 5, 5, 5, 1, 10, 10, 10, 8, 2, 1, 20]))
