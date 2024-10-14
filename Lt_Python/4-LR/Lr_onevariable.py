import numpy as np

def linear_regression(X, y):
    X = np.column_stack((np.ones(X.shape[0]), X))
    theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    return theta[1], theta[0] 

def main():
    X = []
    y = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            x, y_val = map(float, line.split(','))
            X.append(x)
            y.append(y_val)
        except EOFError:
            break

    X = np.array(X)
    y = np.array(y)
    a, b = linear_regression(X, y)
    print(f"{a} {b}")

if __name__ == "__main__":
    main()

