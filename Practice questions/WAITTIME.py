# cook your dish here
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of sets of squats
    K,X = map(int,input().split())
    K*=7
    print(abs(K-X))
