#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i * j
            print(f'{result:4}', end=' ')
        print()  # Move to the next line after each row

if __name__ == "__main__":
    main()
