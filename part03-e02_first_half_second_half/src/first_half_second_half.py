#!/usr/bin/env python3

import numpy as np

def first_half_second_half(arr):
    arr = np.array(arr)
    m = arr.shape[1] // 2
    sum_first_half = np.sum(arr[:, :m], axis=1)
    sum_second_half = np.sum(arr[:, m:], axis=1)
    mask = sum_first_half > sum_second_half
    return arr[mask]

def main():
    input_array = np.array([
        [8, 9, 3, 8, 8, 2],
        [0, 5, 3, 9, 9, 4],
        [5, 7, 6, 0, 4, 1],
        [7, 8, 1, 6, 2, 3],
        [2, 1, 3, 5, 8, 0]
    ])
    
    result = first_half_second_half(input_array)
    print("Resulting array:")
    print(result)

if __name__ == "__main__":
    main()

