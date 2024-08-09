#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    return [row.reshape(1, -1) for row in a]

def get_column_vectors(a):
    return [column.reshape(-1, 1) for column in a.T]

def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (4, 4))
    print("a:", a)
    print("Row vectors:")
    for row_vector in get_row_vectors(a):
        print(row_vector)
    print("Column vectors:")
    for column_vector in get_column_vectors(a):
        print(column_vector)

if __name__ == "__main__":
    main()

