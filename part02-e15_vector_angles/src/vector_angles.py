#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    # Calculate the inner product between pairs of vectors
    inner_product = np.einsum('ij,ij->i', X, Y)
    # Calculate the norms of the vectors in X and Y
    norms_X = scipy.linalg.norm(X, axis=1)
    norms_Y = scipy.linalg.norm(Y, axis=1)
    # Calculate the cosine of the angle between each pair of vectors
    cos_angle = inner_product / (norms_X * norms_Y)
    # To avoid numerical errors, we ensure the cosine values are in the range [-1, 1]
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    # Calculate the angle in radians and then convert to degrees
    angles = np.degrees(np.arccos(cos_angle))
    return angles

def main():
    # Example usage:
    # Let's create two arrays X and Y, each with 3 rows (vectors) and 2 columns (dimensions)
    X = np.array([[1, 2], [3, 4], [5, 6]])
    Y = np.array([[6, 5], [4, 3], [2, 1]])
    
    # Compute the angles between each pair of vectors
    angles = vector_angles(X, Y)
    print(angles)

if __name__ == "__main__":
    main()

