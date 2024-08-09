#!/usr/bin/env python3

import numpy as np

def get_rows(arr):
    return [row for row in arr]

def get_columns(arr):
    return [column for column in arr.T]

def main():
    a = np.array([[5, 0, 3, 3],
                  [7, 9, 3, 5],
                  [2, 4, 7, 6],
                  [8, 8, 1, 6]])

    rows = get_rows(a)
    columns = get_columns(a)

    print("Rows:")
    for row in rows:
        print(row)

    print("Columns:")
    for column in columns:
        print(column)

if __name__ == '__main__':
    main()

