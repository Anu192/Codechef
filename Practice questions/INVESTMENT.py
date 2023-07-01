T = int(input())
for _ in range(T):
    X,Y= map(int,input().split())
    if 2*Y<=X:print("Yes")
    if X<2*Y or X==Y:print("No")
