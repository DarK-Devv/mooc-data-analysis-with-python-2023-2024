#!/usr/bin/env python3

import pandas as pd

def main():
    # Load the data from the TSV file
    file_path = 'src/municipal.tsv'
    df = pd.read_csv(file_path, sep='\t')
    
    # Get the shape of the DataFrame
    rows, columns = df.shape
    
    # Print the shape
    print(f"Shape: {rows},{columns}")
    
    # Print the column names
    print("Columns:")
    for col in df.columns:
        print(col)

# Run the main function to test the solution
if __name__ == "__main__":
    main()
