#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    # Path to the CSV file
    file_path = 'src/kumpula-weather-2017.csv'
    
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Assuming the column for snow depth is named 'Snow depth (cm)' or similar.
    # If the column has a different name, adjust accordingly.
    max_snow_depth = df['Snow depth (cm)'].max()
    
    return max_snow_depth

def main():
    max_snow = snow_depth()
    print(f"Max snow depth: {max_snow:.1f}")

# Ensure the main function is called when this script is executed directly
if __name__ == "__main__":
    main()
