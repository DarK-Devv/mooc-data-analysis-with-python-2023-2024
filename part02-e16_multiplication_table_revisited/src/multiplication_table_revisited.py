#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    # Create two 1D arrays using np.arange
    row = np.arange(n)
    col = np.arange(n)
    
    # Use broadcasting to multiply the row and column vectors
    result = row[:, np.newaxis] * col
    
    return result

# Example usage
print(multiplication_table(4))
