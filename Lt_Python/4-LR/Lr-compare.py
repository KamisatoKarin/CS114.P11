import sys
import time
import importlib
from tabulate import tabulate

# Danh sách các phương pháp cần so sánh
methods = [
    "Lr-findlog2.Lr-cholesky",
    "Lr-findlog2.Lr-gauss-seidel",
    "Lr-findlog2.Lr-qr",
    "Lr-findlog2.Lr-gauss-jordan",
    "Lr-findlog2.Lr-conjugate-gradient",
    "Lr-findlog2.Lr-cramer",
    "Lr-findlog2.Lr-lu",
    "Lr-findlog2.Lr-inverse",
    "Lr-findlog2.Lr-direct-solution",
    "Lr-findlog2.Lr-ridge"
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
    a, b, c = module.linear_regression(X, y)
    end_time = time.time()
    mse = module.mse(X, y, a, b, c)
    return a, b, c, mse, end_time - start_time

def process_input(input_file, output_file):
    X, y = read_input(input_file)

    results = []
    for method in methods:
        try:
            a, b, c, mse, execution_time = run_method(method, X, y)
            method_name = method.split('.')[-1]
            results.append([method_name, a, b, c, mse, execution_time])
        except Exception as e:
            print(f"Error running {method}: {str(e)}")

    # Sắp xếp kết quả theo MSE tăng dần
    results.sort(key=lambda x: x[4])

    # Ghi kết quả vào file
    with open(output_file, 'a') as f:
        f.write(f"\nProcessing {input_file}\n")
        #f.write("Bang 1: Cac he so a, b, c\n")
        #headers_abc = ["Method", "a", "b", "c"]
        #f.write(tabulate([[r[0], r[1], r[2], r[3]] for r in results], headers=headers_abc, floatfmt="") + "\n\n")
        f.write("Bang 2: MSE va thoi gian thuc thi\n")
        headers_mse_time = ["Method", "MSE", "Time (s)"]
        f.write(tabulate([[r[0], r[4], r[5]] for r in results], headers=headers_mse_time, floatfmt="") + "\n\n")

def main():
    output_file = "Lt_Python/4-LR/comparison_results.txt"
    
    # Xóa nội dung cũ của file kết quả nếu nó đã tồn tại
    open(output_file, 'w').close()
    
    input_files = [
        "Lt_Python/4-LR/input/input1.txt",
        "Lt_Python/4-LR/input/input2.txt",
        "Lt_Python/4-LR/input/input3.txt",
        "Lt_Python/4-LR/input/input4.txt",
        "Lt_Python/4-LR/input/input5.txt",
        "Lt_Python/4-LR/input/input6.txt"
    ]

    for input_file in input_files:
        process_input(input_file, output_file)

    print(f"Results have been written to {output_file}")

if __name__ == "__main__":
    main()
