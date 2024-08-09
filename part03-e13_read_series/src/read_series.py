#!/usr/bin/env python3

import pandas as pd

def read_series():
    data = {}
    print("Enter index and value pairs, one per line. Use an empty line to end.")
    
    while True:
        line = input()
        if line == "":
            break
        
        parts = line.split()
        if len(parts) != 2:
            raise ValueError("Malformed input: each line must contain exactly two parts separated by whitespace")
        
        index, value = parts
        data[index] = value
    
    return pd.Series(data, dtype='object')

def main():
    try:
        series = read_series()
        print("Created Series:")
        print(series)
    except ValueError as e:
        print(f"Error: {e}")

# Run the main function to test the solution
if __name__ == "__main__":
    main()
