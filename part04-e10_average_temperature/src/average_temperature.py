#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    # Path to the CSV file
    file_path = 'src/kumpula-weather-2017.csv'
    
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Print out the column names to verify they are correct
    print("Columns in the dataset:", df.columns)
    
    # Check if 'Year', 'm', 'd', and 'Air temperature (degC)' columns exist
    if 'Year' not in df.columns or 'm' not in df.columns or 'd' not in df.columns or 'Air temperature (degC)' not in df.columns:
        raise ValueError("The required columns are not present in the dataset.")
    
    # Rename columns to year, month, and day
    df.rename(columns={'Year': 'year', 'm': 'month', 'd': 'day'}, inplace=True)
    
    # Create a 'Date' column from 'year', 'month', and 'day'
    df['Date'] = pd.to_datetime(df[['year', 'month', 'day']])
    
    # Filter for the month of July
    july_df = df[df['Date'].dt.month == 7]
    
    # Calculate the average temperature in July
    average_temp = july_df['Air temperature (degC)'].mean()
    
    return average_temp

def main():
    try:
        avg_temp = average_temperature()
        print(f"Average temperature in July: {avg_temp:.1f}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ensure the main function is called when this script is executed directly
if __name__ == "__main__":
    main()
