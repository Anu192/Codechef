T = int(input())
for _ in range(T):
    X = str(input())
    Y = str(input())
    for i in range(5):
        if X[i]==Y[i]:print("G",end="")
        else:print("B",end="")
    print("")