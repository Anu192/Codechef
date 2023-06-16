T = int(input())
for _ in range(T):
    X,Y,Z= map(int,input().split())
    print((2*(180+X))-(Y+Z))
