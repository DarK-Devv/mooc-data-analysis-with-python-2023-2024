#!/usr/bin/env python3

import numpy as np
from collections import Counter

def most_frequent_first(arr, c):
    arr = np.array(arr)
    col_c = arr[:, c]
    frequency = Counter(col_c)
    sorted_elements_by_freq = [item for item, count in frequency.most_common()]
    sort_index = np.argsort([sorted_elements_by_freq.index(x) for x in col_c])
    sorted_arr = arr[sort_index]
    
    return sorted_arr

def main():
    a = np.array([
        [5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
        [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
        [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
        [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
        [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
        [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
        [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
        [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
        [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
        [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]
    ])
    
    c = 1
    
    result = most_frequent_first(a, c)
    print("Sorted array based on frequency in column", c)
    print(result)

if __name__ == "__main__":
    main()
