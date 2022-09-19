import numpy as np

def de_jong(t, r, a=0.1, b=0.2, c=0.2, d=0.1):
    x = r[0]
    y = r[1]
    z = r[2]
    return np.array([np.sin(a * y) - np.cos(b * x), np.sin(c * x) - np.cos(d * y), 0])

def clifford(t, r, a=0.1, b=0.2, c=0.3, d=0.4):
    x = r[0]
    y = r[1]
    z = r[2]
    return np.array([np.sin(a * y) + c * np.cos(a * x), np.sin(b * x) + d * np.cos(b * y), 0])

def lotka_volterra(t, r):
    x = r[0]
    y = r[1]
    z = r[2]
    return np.array([x * (1 - x - 9 * y), -y * (1 - 6 * x - y + 9 * z), z * (1 - 3 * x - z)])

def lorenz(t, r, sigma=10, rho=28, beta=8/3):
    x = r[0]
    y = r[1]
    z = r[2]
    return np.array([sigma * (y - x), x * (rho - z) - y, (x * y) - (beta * z)])

def rossler(t, r, a = 0.2, b = 0.2, c = 5.7):
    x = r[0]
    y = r[1]
    z = r[2]
    return np.array([- y - z, x + a * y, b + z * (x - c)])