import numpy as np

def Mystery(Arr):
    n = len(Arr)
    x = 0
    for i in range(0, n - 2):
      print(i)
      for j in range(i + 1, n - 1):
        x = x + 1
          #if (Arr[i,j] != Arr[j,i]):
            #return False
            #print('Out: %d - %d' % (i, j))
    #return True
    return x

Arr = np.zeros((5,5))
Arr[1,3] = 1
Arr[3,1] = 1
print(Arr)
print(Mystery(Arr))
