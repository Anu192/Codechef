# cook your dish here
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of sets of squats
    X,Y = map(int,input().split())

    # Calculate the total number of squats
    total_squats = X /10

    # Print the result
    print(int(total_squats*Y))
