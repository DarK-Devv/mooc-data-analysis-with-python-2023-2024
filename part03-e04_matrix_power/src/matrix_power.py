#!/usr/bin/env python3


import numpy as np
from functools import reduce

def matrix_power(a, n):
    a = np.array(a)
    
    if n == 0:
        return np.eye(a.shape[0])
    elif n > 0:
        return reduce(np.matmul, (a for _ in range(n)))
    else:
        a_inv = np.linalg.inv(a)
        return reduce(np.matmul, (a_inv for _ in range(abs(n))))

def main():
    a = np.array([
        [2, 1],
        [1, 2]
    ])
    
    n = 3
    
    result_pos = matrix_power(a, n)
    print(f"Matrix raised to the power {n}:")
    print(result_pos)
    
    n_neg = -1
    
    result_neg = matrix_power(a, n_neg)
    print(f"Matrix raised to the power {n_neg}:")
    print(result_neg)
    
    n_zero = 0
    
    result_zero = matrix_power(a, n_zero)
    print(f"Matrix raised to the power {n_zero}:")
    print(result_zero)

if __name__ == "__main__":
    main()
