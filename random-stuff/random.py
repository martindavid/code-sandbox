def sim(string1, string2):
    lf = len(string1)
    lr = len(string2)
    A = [[0 for x in range(0,lr)] for y in range(0,lf)] 
    A[0][0] = 0
    for j in range(1, lf):
        A[j][0] = j * 1

    for k in range(1, lr):
        A[0][k] = k * 4

    return A


Arr = sim("led","deed")
for a in Arr:
    print(a)
print(Arr[1][0])
print(Arr[0][1])
