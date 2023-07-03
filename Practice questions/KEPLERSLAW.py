T = int(input())
for _ in range(T):
    X,Y,Z,A = map(int,input().split())
    if X**2/Z**3==Y**2/A**3:print("Yes")
    else:print("No")
