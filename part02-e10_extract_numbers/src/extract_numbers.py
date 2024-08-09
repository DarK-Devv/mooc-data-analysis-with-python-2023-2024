#!/usr/bin/env python3

def extract_numbers(s):
    words = s.split()
    numbers = []

    for word in words:
        try:
            num = int(word)
            numbers.append(num)
        except ValueError:
            try:
                num = float(word)
                numbers.append(num)
            except ValueError:
                pass

    return numbers

def main():
    result = extract_numbers("abd 123 1.2 test 13.2 -1")
    print(result)

if __name__ == "__main__":
    main()

