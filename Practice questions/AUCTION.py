T = int(input())
for _ in range(T):
    X,Y,Z= map(int,input().split())
    a=max(X,Y,Z)
    if a==X:print("Alice")
    elif a==Y:print("Bob")
    elif a==Z:print("Charlie")
