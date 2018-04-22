def triangleOrNot(a, b, c):
    n = len(a)
    result = []
    for i in range(n):
        side_a = a[i]
        side_b = b[i]
        side_c = c[i]
        print(side_a,side_b,side_c)
        sort_arr = qsort([side_a,side_b,side_c])
        print(sort_arr)
        result.append('No' if (sort_arr[0] + sort_arr[1] <= sort_arr[2]) else 'Yes')

    return result

def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


print('Result : ',triangleOrNot([7,10,7],[2,3,4],[2,7,4]))
