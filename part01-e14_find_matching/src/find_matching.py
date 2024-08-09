#!/usr/bin/env python3

def find_matching(L, pattern):
    indices = []
    for index, string in enumerate(L):
        if pattern in string:
            indices.append(index)
    return indices

def main():
    L = ["sensitive", "engine", "rubbish", "comment"]
    pattern = "en"
    result = find_matching(L, pattern)
    print(result)

if __name__ == "__main__":
    main()

