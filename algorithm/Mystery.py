import numpy as np

def Mystery(arr):
  n = len(arr)
  for i in range(n - 2):
    for j in range(i + 1, n - 1):
      print('%d - %d' % (i, j))
     # if arr[i, j] != arr[j, i]:
       # return False
  #return True
      #print('%d - %d' % (i, j))

Arr = np.zeros((5,5))
Arr[0,1] = 1
print(Arr)
print(Mystery(Arr))
