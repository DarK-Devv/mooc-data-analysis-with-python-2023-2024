#!/usr/bin/python3

import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    # Coefficients matrix for the system
    A = np.array([
        [a1, -1],
        [a2, -1]
    ])
    # Constants matrix for the system
    B = np.array([-b1, -b2])
    
    # Solve the least squares problem
    solution, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)
    
    # Extract x and y from the solution
    x, y = solution
    # Check if the residuals are very close to zero indicating an exact intersection
    exact = np.isclose(residuals, 0).all()
    
    return (x, y), exact

def main():
    a1 = 1
    b1 = 2
    a2 = -1
    b2 = 0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1 = a2 = 1
    b1 = 2
    b2 = -2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1 = 1
    b1 = 2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1 = 1
    b1 = 2
    a2 = 1
    b2 = 1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()

