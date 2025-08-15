import numpy as np

def portfolio_variance(weights, cov):
    return weights.T @ cov @ weights

def portfolio_return(weights, returns):
    return weights @ returns

def optimize_portfolio(returns, cov, target_return, steps=20):
    n = len(returns)
    best_var = float('inf')
    best_weights = None

    def search(index, current_weights, current_sum, current_return):
        nonlocal best_var, best_weights
        if index == n - 1:
            w = 1 - current_sum
            if 0 <= w <= 1:
                weights = np.array(current_weights + [w])
                port_return = portfolio_return(weights, returns)
                if port_return >= target_return:
                    var = portfolio_variance(weights, cov)
                    if var < best_var:
                        best_var = var
                        best_weights = weights
            return
        for step in range(steps + 1):
            w = step / steps
            if current_sum + w > 1:
                break
            search(index + 1, current_weights + [w], current_sum + w, current_return + w * returns[index])

    search(0, [], 0, 0)
    return best_weights, best_var

def main():
    n = int(input("Number of assets: "))
    returns = []
    print("Enter expected returns (decimal) for each asset:")
    for i in range(n):
        r = float(input(f"Asset {i+1}: "))
        returns.append(r)
    returns = np.array(returns)

    print("Enter covariance matrix row by row (space separated):")
    cov = []
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        cov.append(row)
    cov = np.array(cov)

    target_return = float(input("Enter target portfolio return (decimal): "))

    weights, var = optimize_portfolio(returns, cov, target_return)

    if weights is None:
        print("No portfolio found meeting target return.")
    else:
        print("\nOptimal portfolio weights:")
        for i, w in enumerate(weights):
            print(f"Asset {i+1}: {w:.4f}")
        print(f"Portfolio variance: {var:.6f}")

if __name__ == "__main__":
    main()
