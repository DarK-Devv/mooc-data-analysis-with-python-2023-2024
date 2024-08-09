#!/usr/bin/env python3

import pandas as pd

def below_zero():
    # Path to the CSV file
    file_path = 'src/kumpula-weather-2017.csv'
    
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Check if 'Air temperature (degC)' column exists
    if 'Air temperature (degC)' not in df.columns:
        raise ValueError("The required column is not present in the dataset.")
    
    # Filter the data to find days with temperature below zero
    below_zero_days = df[df['Air temperature (degC)'] < 0]
    
    # Count the number of such days
    num_below_zero_days = below_zero_days.shape[0]
    
    return num_below_zero_days

def main():
    try:
        num_days = below_zero()
        print(f"Number of days below zero: {num_days}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ensure the main function is called when this script is executed directly
if __name__ == "__main__":
    main()
