import numpy as np

def normalize_data(X):
    return (X - np.mean(X)) / np.std(X)

def ridge_regression(X, y, alpha=1e5):
    X = np.column_stack((np.ones(X.shape[0]), X))
    I = np.eye(X.shape[1])
    I[0, 0] = 0 
    coefficients = np.linalg.inv(X.T.dot(X) + alpha * I).dot(X.T).dot(y)
    return coefficients[1], coefficients[0]

def linear_regression(X, y):
    X_normalized = normalize_data(X)
    a_norm, b_norm = ridge_regression(X_normalized, y)
    
    return a_norm, b_norm

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
