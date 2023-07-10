T = int(input())
for _ in range(T):
    X= int(input())
    Y=str(input())
    Z=int(X/2)
    if Y[0:Z]==Y[Z:]:print("YES")
    else:print("NO")
