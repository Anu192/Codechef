T = int(input())
for _ in range(T):
    X= int(input())
    Y= int(input())
    empty = []
    while Y > 0:
        Y, remd = divmod(Y, 10)
        empty.append(remd)
    if 0 in empty or 5 in empty:print("Yes")
    else:print("No")
    
