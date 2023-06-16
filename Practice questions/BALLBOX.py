h=int(input())
for i in range(h):
    n,k=map(int,input().split())
    p=(k*(k+1))/2
    if n<=k and n!=1 and k!=1:
        print('no')
    elif n>=p:
        print('yes')
    else:
        print('no')