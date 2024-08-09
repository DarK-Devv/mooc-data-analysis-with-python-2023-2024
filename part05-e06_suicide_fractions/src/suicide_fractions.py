#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    # Load the data set
    file_path = 'src/who_suicide_statistics.csv'
    df = pd.read_csv(file_path)
    
    df['suicide_fraction'] = df['suicides_no'] / df['population']
    
    result = df.groupby('country')['suicide_fraction'].mean()
    
    return result

def main():
    suicide_fractions_series = suicide_fractions()
    print(suicide_fractions_series)

if __name__ == "__main__":
    main()
