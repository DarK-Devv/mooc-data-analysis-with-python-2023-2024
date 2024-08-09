#!/usr/bin/env python3

import pandas as pd

def split_date():
    # Path to the CSV file
    file_path = 'src/Helsingin_pyorailijamaarat.csv'
    
    # Read the dataset
    df = pd.read_csv(file_path, delimiter=';')
    
    # Remove any empty rows at the end
    df = df.dropna(how='all')
    
    # Remove columns that contain only missing values
    df = df.dropna(axis=1, how='all')
    
    # Split the 'Päivämäärä' column
    date_df = df['Päivämäärä'].str.split(expand=True)
    
    # Rename columns
    date_df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    
    # Mapping for Weekday and Month
    weekday_map = {
        'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu',
        'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'
    }
    month_map = {
        'tammi': '1', 'helmi': '2', 'maalis': '3', 'huhti': '4',
        'touko': '5', 'kesä': '6', 'heinä': '7', 'elo': '8',
        'syys': '9', 'loka': '10', 'marras': '11', 'joulu': '12'
    }
    
    # Apply mappings
    date_df['Weekday'] = date_df['Weekday'].map(weekday_map)
    date_df['Month'] = date_df['Month'].map(month_map)
    
    # Convert Day, Month, Year to integers
    date_df['Day'] = date_df['Day'].astype(int)
    date_df['Month'] = date_df['Month'].astype(int)
    date_df['Year'] = date_df['Year'].astype(int)
    
    # Extract Hour and convert to integer
    date_df['Hour'] = date_df['Hour'].str.slice(0, 2).astype(int)
    
    return date_df

def main():
    df = split_date()
    print(df)

if __name__ == "__main__":
    main()
