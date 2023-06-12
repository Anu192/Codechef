# cook your dish here
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of sets of squats
    X,Y,Z = map(int,input().split())
    print(4*X+2*Y+0*Z)
