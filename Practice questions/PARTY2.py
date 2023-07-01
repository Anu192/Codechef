T = int(input())
for _ in range(T):
    N,X,K= map(int,input().split())
    if N*X<=K:print("YES")
    else:print("NO")