#!/usr/bin/env python3

def main():
    pairs = [(die1, die2) for die1 in range(1, 7) for die2 in range(1, 7) if die1 + die2 == 5]
    for pair in pairs:
        print(pair)

if __name__ == "__main__":
    main()

