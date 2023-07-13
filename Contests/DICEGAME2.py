# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the dice rolls for Alice and Bob
    A1, A2, A3, B1, B2, B3 = map(int, input().split())

    # Calculate the score for Alice
    alice_score = sum(sorted([A1, A2, A3])[1:])

    # Calculate the score for Bob
    bob_score = sum(sorted([B1, B2, B3])[1:])

    # Compare the scores and print the result
    if alice_score > bob_score:
        print("Alice")
    elif bob_score > alice_score:
        print("Bob")
    else:
        print("Tie")
