for i in range(int(input())):
    x,y,a=map(int, input().split())
    if(a>=x and a<y):
        print("Yes")
    else:
        print("No")