#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    # Calculate the square of each element and sum along axis 1
    squares_sum = np.sum(a**2, axis=1)
    
    # Calculate the square root of the sum to get the Euclidean norm
    lengths = np.sqrt(squares_sum)
    
    return lengths

def main():
    # Test your function with a sample input array
    input_array = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
    
    result = vector_lengths(input_array)
    
    # Print the result
    print("Vector Lengths:")
    print(result)

if __name__ == "__main__":
    main()
