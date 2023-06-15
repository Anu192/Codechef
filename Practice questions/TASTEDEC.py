# cook your dish here
# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of sets of squats
    X,Y = map(int,input().split())
    x=X*2
    y=Y*5
    if x>y:print("Chocolate")
    elif x<y:print("candy")
    else:print("Either")