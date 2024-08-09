#!/usr/bin/env python3
import pandas as pd
import numpy as np

def capitalize_name(name):
    parts = name.split(', ')
    parts = [part.split() for part in parts]
    capitalized_parts = [' '.join(word.capitalize() for word in part) for part in parts]
    return ' '.join(capitalized_parts[::-1])

def cleaning_data():
    # Path to the TSV file
    file_path = 'src/presidents.tsv'
    
    # Read the dataset
    df = pd.read_csv(file_path, delimiter='\t')
    
    # Clean the 'President' column
    df['President'] = df['President'].apply(capitalize_name)
    
    # Clean the 'Vice-president' column
    df['Vice-president'] = df['Vice-president'].apply(capitalize_name)
    
    # Convert 'Start' to integer
    df['Start'] = df['Start'].str.extract(r'(\d{4})').astype(int)
    
    # Convert 'Last' to float, replacing '-' with NaN
    df['Last'] = df['Last'].replace('-', np.nan).astype(float)
    
    # Convert 'Seasons' to integer
    df['Seasons'] = df['Seasons'].replace('two', '2').astype(int)
    
    return df

def main():
    df = cleaning_data()
    print(df)

if __name__ == "__main__":
    main()
