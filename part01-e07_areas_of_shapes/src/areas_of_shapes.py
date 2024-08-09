#!/usr/bin/env python3

import math

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ").lower()

        if shape == "":
            break

        if shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = calculate_triangle_area(base, height)
        elif shape == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = calculate_rectangle_area(width, height)
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            area = calculate_circle_area(radius)
        else:
            print("Unknown shape!")
            continue

        print(f"The area is {area:.6f}")

if __name__ == "__main__":
    main()

