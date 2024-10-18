import sys
import time
import importlib
from tabulate import tabulate

# Danh sách các phương pháp cần so sánh
methods = [
    "Lr-findx^4.Lrx-gauss-jordan",
    "Lr-findx^4.Lrx-cramer",
    "Lr-findx^4.Lrx-lu",
    "Lr-findx^4.Lrx-inverse",
    "Lr-findx^4.Lrx-direct-solution",
]

def read_input(filename):
    X = []
    y = []
    with open(filename, 'r') as f:
        for line in f:
            x, y_val = map(float, line.strip().split(','))
            X.append(x)
            y.append(y_val)
    return X, y

def run_method(method_name, X, y):
    module = importlib.import_module(method_name)
    start_time = time.time()
    a, b, c, d = module.linear_regression(X, y)
    end_time = time.time()
    mse = module.mse(X, y, a, b, c, d)
    return a, b, c, d, mse, end_time - start_time

def process_input(input_file, output_file1, output_file2):
    X, y = read_input(input_file)

    results = []
    for method in methods:
        try:
            a, b, c, d, mse, execution_time = run_method(method, X, y)
            results.append([method, a, b, c, d, mse, execution_time])
        except Exception as e:
            print(f"Error running {method}: {str(e)}")

    # Sắp xếp kết quả theo MSE tăng dần
    results.sort(key=lambda x: x[5])

    # Ghi kết quả vào file
    with open(output_file1, 'a') as f:
        f.write(f"\nProcessing {input_file}\n")
        f.write("Bang 1: Cac he so a, b, c, d\n")
        headers_abcd = ["Method", "a", "b", "c", "d"]
        f.write(tabulate([[r[0], r[1], r[2], r[3], r[4]] for r in results], headers=headers_abcd, floatfmt="") + "\n\n")
    
    with open(output_file2, 'a') as f:
        f.write(f"\nProcessing {input_file}\n")
        f.write("Bang 2: MSE va thoi gian thuc thi\n")
        headers_mse_time = ["Method", "MSE", "Time (s)"]
        f.write(tabulate([[r[0], r[5], r[6]] for r in results], headers=headers_mse_time, floatfmt="") + "\n\n")

def main():
    output_file1 = "Lt_Python/4-LR/comparison_results1.txt"
    output_file2 = "Lt_Python/4-LR/comparison_results2.txt"
    
    # Xóa nội dung cũ của file kết quả nếu nó đã tồn tại
    open(output_file1, 'w').close()
    open(output_file2, 'w').close()
    
    input_files = [
        "Lt_Python/4-LR/input/input1.txt",
        "Lt_Python/4-LR/input/input2.txt",
        "Lt_Python/4-LR/input/input3.txt",
        "Lt_Python/4-LR/input/input4.txt",
        "Lt_Python/4-LR/input/input5.txt",
        "Lt_Python/4-LR/input/input6.txt"
    ]

    for input_file in input_files:
        process_input(input_file, output_file1, output_file2)

    print(f"Results have been written to {output_file1} and {output_file2}")

if __name__ == "__main__":
    main()
