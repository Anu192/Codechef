T = int(input())
for _ in range(T):
    X,Y= map(int,input().split())
    if X>=Y:print(7-X)
    else:print(7-Y)
