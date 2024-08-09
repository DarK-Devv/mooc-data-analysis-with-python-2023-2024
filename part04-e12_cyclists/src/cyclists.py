#!/usr/bin/env python3

import pandas as pd

def cyclists():
    # Path to the CSV file
    file_path = 'src/Helsingin_pyorailijamaarat.csv'
    
    # Read the dataset with the correct delimiter
    df = pd.read_csv(file_path, delimiter=';')
    
    # Remove any empty rows at the end
    df = df.dropna(how='all')
    
    # Remove columns that contain only missing values
    df = df.dropna(axis=1, how='all')
    
    return df

def main():
    try:
        cleaned_df = cyclists()
        print(cleaned_df)
    except Exception as e:
        print(f"An error occurred: {e}")

# Ensure the main function is called when this script is executed directly
if __name__ == "__main__":
    main()
