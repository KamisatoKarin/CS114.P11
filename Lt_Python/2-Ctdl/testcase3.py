import random

def generate_test_case(num_cases):
    actions = [1, 2, 3]
    test_cases = []
    
    for _ in range(num_cases):
        action = random.choice(actions)
        player_id = random.randint(1, 100000000)  # Generate a random integer for player_id
        test_cases.append(f"{action} {player_id}")
    
    # Add the termination line
    test_cases.append("0")
    
    return test_cases

def main():
    num_cases = 500000  # You can change this to generate more or fewer test cases
    test_cases = generate_test_case(num_cases)
    
    # Write the test cases to a file
    with open("testcase3.txt", "w") as file:
        for case in test_cases:
            file.write(case + "\n")

if __name__ == "__main__":
    main()