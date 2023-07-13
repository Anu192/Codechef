def is_divisible(A, B):
    return A % B == 0
def find_AB_pairs():
    T = int(input())
    for _ in range(T):
        X, Y, Z = map(int, input().split())
        if is_divisible(X * Y, Z):
            print(X * Y, Z)
            continue
        if is_divisible(Y * Z, X):
            print(Y * Z, X)
            continue
        if is_divisible(X * Z, Y):
            print(X * Z, Y)
            continue
        
        print(-1)

find_AB_pairs()
