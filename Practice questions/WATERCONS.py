# cook your dish here
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of sets of squats
    X = int(input())
    if X>=2000:
        print("YES")
    else:
        print("NO")
