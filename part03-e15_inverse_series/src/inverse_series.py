#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    # Create a new Series by swapping the index and values
    # If a value appears multiple times, the last occurrence will be used
    inverted = pd.Series(s.index, index=s.values)
    return inverted

def main():
    # Create a test Series
    d = {2001: "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017: "Trump"}
    s = pd.Series(d, name="Presidents")
    
    # Print the original Series
    print("Original Series:")
    print(s)
    
    # Invert the Series
    inverted_s = inverse_series(s)
    
    # Print the inverted Series
    print("\nInverted Series:")
    print(inverted_s)

# Run the main function to test the solution
if __name__ == "__main__":
    main()
