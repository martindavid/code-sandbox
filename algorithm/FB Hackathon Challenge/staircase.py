def staircase(n):
    i = 1
    while i <= n:
        for j in range(n, 0, -1):
            if j <= i:
                print("#", end="")
            else:
                print(" ", end="")
        print("")
        i = i + 1

staircase(6)