# cook your dish here
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of sets of squats
    P,M,V = map(int,input().split())
    print((M-P+1)*V)
