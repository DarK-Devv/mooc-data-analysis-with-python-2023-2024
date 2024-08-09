#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    # Create a dictionary to hold the data for the DataFrame
    data = {i: s**i for i in range(1, k+1)}
    
    # Create the DataFrame
    df = pd.DataFrame(data)
    
    return df

def main():
    # Example Series
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    
    # Generate the DataFrame with powers from 1 to 3
    result = powers_of_series(s, 3)
    
    # Print the resulting DataFrame
    print(result)

# Run the main function to test the solution
if __name__ == "__main__":
    main()
