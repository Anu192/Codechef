T = int(input())
for _ in range(T):
    A,B= map(int,input().split())
    if (A+B)%2==0:print("YES")
    else:print("NO")
