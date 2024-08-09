#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
    return line_count, word_count, char_count

def main():
    for filename in sys.argv[1:]:
        line_count, word_count, char_count = file_count(filename)
        print(f"{line_count}\t{word_count}\t{char_count}\t{filename}")

if __name__ == '__main__':
    main()
