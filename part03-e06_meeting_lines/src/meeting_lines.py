#!/usr/bin/python3

import numpy as np

def meeting_lines(a1, b1, a2, b2):
    # Coefficients matrix
    A = np.array([[a1, -1], [a2, -1]])
    # Constants matrix
    B = np.array([-b1, -b2])
    
    # Solve the system of equations
    solution = np.linalg.solve(A, B)
    
    # Extract x and y from the solution
    x, y = solution
    return x, y

def main():
    # Example coefficients for the lines
    a1, b1 = 1, 2
    a2, b2 = -1, 3
    
    # Find the meeting point
    x, y = meeting_lines(a1, b1, a2, b2)
    print(f"The lines meet at the point ({x}, {y})")

# Run the main function to test the solution
if __name__ == "__main__":
    main()
