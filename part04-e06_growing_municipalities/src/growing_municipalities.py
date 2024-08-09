#!/usr/bin/env python3
import pandas as pd

def growing_municipalities(file_path):
   
    # Read the data from the TSV file
    df = pd.read_csv(file_path, sep='\t')
    
    # Debugging: Print the actual columns of the DataFrame
    print("DataFrame columns:", df.columns)
    
    # Check if the expected columns are in the DataFrame
    if 'previous_population' in df.columns.tolist() and 'current_population' in df.columns.tolist():
        growing = df['current_population'] > df['previous_population']
    else:
        raise ValueError("DataFrame must contain columns: 'previous_population' and 'current_population'")
    
    proportion_growing = growing.mean()
    return proportion_growing

def main():
    # File path to the data file
    file_path = 'src/municipal.tsv'  # Update this path as necessary
    
    # Calculate the proportion of growing municipalities
    proportion = growing_municipalities(file_path)
    print(f"Proportion of growing municipalities: {proportion * 100:.1f}%")

if __name__ == "__main__":
    main()
