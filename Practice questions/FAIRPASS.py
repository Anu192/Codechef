T = int(input())
for _ in range(T):
    X,Y= map(int,input().split())
    if X>=Y or Y<X:print("NO")
    else:print("YES")
