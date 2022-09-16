import numpy as np

def lyapunov_exponent(x, r):
    return np.log(np.abs(r - 2 * r * x))
    
def logistic_map(x, r):
    return x * r * (1 - x)

def log_map_iter(n, x, r):
    exponents = []
    for i in range(1, n):
        x = logistic_map(x=x, r=r)
        exponents.append(lyapunov_exponent(x=x, r=r))
    return x, exponents

def growth_rate(n=100, n_iter=20, seed=0.1, xmin=1, xmax=4, dr=0.01):
    maps, lambdas = [], []
    rvalues = np.arange(start=xmin, stop=xmax, step=dr)
    for r in rvalues:
        x, result = log_map_iter(n=n, x=seed, r=r)
        lambdas.append(np.mean(result))
        for t in range(n_iter):
            x = logistic_map(x=x, r=r)
            maps.append(x)  
    return maps, lambdas, rvalues