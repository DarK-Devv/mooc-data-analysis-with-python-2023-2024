#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    # Load the data from the TSV file with the region names as the index
    file_path = 'src/municipal.tsv'
    df = pd.read_csv(file_path, sep='\t', index_col=0)
    
    # Find the range of municipalities from Akaa to Äänekoski
    start = df.index.get_loc("Akaa")
    end = df.index.get_loc("Äänekoski")
    
    # Return the DataFrame containing only rows about municipalities
    return df.iloc[start:end + 1]

def main():
    # Load the DataFrame
    municipalities_df = municipalities_of_finland()
    
    # Print the shape of the DataFrame
    rows, columns = municipalities_df.shape
    print(f"Shape: {rows},{columns}")
    
    # Print the column names
    print("Columns:")
    for col in municipalities_df.columns:
        print(col)
    
    # Print the first few rows of the DataFrame to verify
    print(municipalities_df.head())

# Run the main function to test the solution
if __name__ == "__main__":
    main()
