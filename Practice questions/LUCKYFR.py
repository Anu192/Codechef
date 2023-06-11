T = int(input())
for i in range(T):
    a = int(input())
    c = 0
    while(a>0):
        r = a%10
        if (r == 4):
            c = c+1
        a = a//10
    print(c)
