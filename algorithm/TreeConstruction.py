def constructTree(degree):
    length = len(degree)
    indexList = [x for x in range(length)]
    result = list()
    for i in range(0,length + 1):
        result.append( list() )

    selectionSort2(degree, indexList)

    for i in range(0, length):
        #print i

        if (i == length - 1):
            result[indexList[i - 1]].append(i -1)
            result[indexList[i]].append(i)
            degree[i - 1] -= 1
            degree[i] -= 1
        else:
            for j in range(0, length):
                if (degree[i] > 0 and degree[j] > degree[i]):
                    result[indexList[i]].append(j)
                    result[indexList[j]].append(i)
                    degree[j] -= 1
                    degree[i] -= 1
                print result

    return result

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


#testCase = [4,1,1,2,2,1,2,1]
testCase2 = [1,2,2,1,1,3]
#print constructTree(testCase)
print constructTree(testCase2)
