#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real solutions
    elif discriminant == 0:
        x = -b / (2*a)
        return (x, x)  # One real solution repeated
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return (x1, x2)  # Two real solutions

if __name__ == "__main__":
    # Test cases
    print(solve_quadratic(1, -3, 2))  # Should print (2.0, 1.0)
    print(solve_quadratic(1, 2, 1))   # Should print (-1.0, -1.0)

