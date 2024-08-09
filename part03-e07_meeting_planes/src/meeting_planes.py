#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    # Coefficients matrix
    A = np.array([
        [a1, b1, -1],
        [a2, b2, -1],
        [a3, b3, -1]
    ])
    # Constants matrix
    B = np.array([-c1, -c2, -c3])
    
    # Solve the system of equations
    solution = np.linalg.solve(A, B)
    
    # Extract y, x, and z from the solution
    y, x, z = solution
    return x, y, z

def main():
    # Example coefficients for the planes
    a1, b1, c1 = 1, 2, 3
    a2, b2, c2 = 4, 5, 6
    a3, b3, c3 = 7, 8, 9
    
    # Find the meeting point
    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"The planes meet at the point ({x}, {y}, {z})")

# Run the main function to test the solution
if __name__ == "__main__":
    main()

