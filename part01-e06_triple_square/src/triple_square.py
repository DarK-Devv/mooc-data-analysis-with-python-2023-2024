#!/usr/bin/env python3


# Part 1: Define the triple and square functions
def triple(x):
    return x * 3

def square(x):
    return x ** 2

def main():
    for value in range(1, 11):
        triple_result = triple(value)
        square_result = square(value)

        if square_result > triple_result:
            break  # Stop the iteration

        print(f'triple({value})=={triple_result} square({value})=={square_result}')

if __name__ == "__main__":
    main()

