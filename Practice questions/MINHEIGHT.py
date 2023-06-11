# cook your dish here
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of sets of squats
    X,H = map(int,input().split())
    if X>=H:
        print("YES")
    else:print("NO")
   
