import random
import os

def generate_large_number(num_digits):
    return ''.join(random.choice('123456789') if i == 0 else random.choice('0123456789') for i in range(num_digits))

def write_testcase_to_file(filename, num_digits):
    large_number = generate_large_number(num_digits)
    with open(filename, 'w') as f:
        f.write(large_number + '\n')

if __name__ == "__main__":
    num_digits = 10000  # Số chữ số của số lớn
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, 'testcase4.txt')
    write_testcase_to_file(filename, num_digits)
    print(f"Testcase with {num_digits} digits written to {filename}")