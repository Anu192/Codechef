# cook your dish here
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of sets of squats
    X,Y = map(int,input().split())
    if X>Y:
        print(X-Y)
    else:
        print("0")