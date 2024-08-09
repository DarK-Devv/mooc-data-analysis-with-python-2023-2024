#!/usr/bin/env python3

import numpy as np

def column_comparison(arr):
    arr = np.array(arr)
    mask = arr[:, 1] > arr[:, -2]
    return arr[mask]

def main():
    input_array = np.array([
        [8, 9, 3, 8, 8],
        [0, 5, 3, 9, 9],
        [5, 7, 6, 0, 4],
        [7, 8, 1, 6, 2],
        [2, 1, 3, 5, 8]
    ])
    
    result = column_comparison(input_array)
    print("Resulting array:")
    print(result)

if __name__ == "__main__":
    main()

