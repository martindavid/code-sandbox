def SelectionSort(text):
    unsortedArray = list(text);
    length = len(unsortedArray)
    for i in range(length):
        min = i
        for j in range(i, length):
            if (unsortedArray[j] < unsortedArray[min]):
                min = j
        #print unsortedArray[min];
        if min != i:
            unsortedArray[i], unsortedArray[min] = unsortedArray[min], unsortedArray[i]
    return unsortedArray

print SelectionSort('SORTXAMPLE')



def selectionSort2(alist, indexList):
   for fillslot in range(len(alist)-1, 0, -1):
       positionOfMax = 0
       for location in range(1,fillslot+1):
           if alist[location] > alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       temp2 = indexList[fillslot]
       alist[fillslot] = alist[positionOfMax]
       indexList[fillslot] = indexList[positionOfMax]
       alist[positionOfMax] = temp
       indexList[positionOfMax] = temp2

indexList = [1,2,3,4,5,6,7,8,9]
alist = [54,26,93,17,77,31,44,55,20]
selectionSort2(alist, indexList)
print(alist)
print indexList
