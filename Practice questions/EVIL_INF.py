def inpx():
    return int(input())

mod=1000000007

NN = 2*10**5 + 10
x = [0]*NN
y = [0]*NN
id = [0]*NN
dp = [0]*NN

for _ in range(int(input())):
    n = int(input())
    x[1:n+1] = map(int, input().split())
    y[1:n+1] = map(int, input().split())
    id[1:n+1] = range(1, n+1)
    id[1:n+1] = sorted(id[1:n+1], key=lambda u: y[u])
    mn = x[id[n]]
    pos = n
    for i in range(n-1, 0, -1):
        if mn < y[id[i]]:
            dp[i] = dp[pos] + 1
        if mn > x[id[i]]:
            mn = x[id[i]]
            pos = i
    mx = max(dp[1:n+1])
    print(mx)
    dp[1:n+1] = [0]*n
