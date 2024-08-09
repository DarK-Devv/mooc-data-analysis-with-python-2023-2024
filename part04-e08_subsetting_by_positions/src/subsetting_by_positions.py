#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    # Path to the TSV file
    file_path = 'src/UK-top40-1964-1-2.tsv'
    
    # Read the dataset with the correct delimiter
    df = pd.read_csv(file_path, delimiter='\t')
    
    # Select the top 10 entries and only the columns Title and Artist
    subset_df = df[['Title', 'Artist']].iloc[:10]
    
    return subset_df

def main():
    result = subsetting_by_positions()
    print(result)
    return result

# Ensure the main function is called when this script is executed directly
if __name__ == "__main__":
    main()
