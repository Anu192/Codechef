# cook your dish here
T=int(input())
for i in range(T):
    A, B = map(int,input().split()) 
    if A+B>6:
        print("YES")
    else:
        print("NO")