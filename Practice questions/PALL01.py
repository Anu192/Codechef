T = int(input())
for _ in range(T):
    X= int(input())
    s=str(X)
    if s == s[::-1]:
        print("wins")
    else:print("loses")
