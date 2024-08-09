#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners(file_path='src/municipal.tsv'):
    # Read the TSV file
    df = pd.read_csv(file_path, sep='\t')
    
    # Set the correct column names
    df.columns = [
        'Region', 'Population', 'Population change from the previous year, %',
        'Share of Swedish-speakers of the population, %',
        'Share of foreign citizens of the population, %',
        'Proportion of the unemployed among the labour force, %',
        'Proportion of pensioners of the population, %'
    ]
    
    # Setting the 'Region' column as the index
    df.set_index('Region', inplace=True)
    
    # Drop rows that are not municipalities by filtering out summary rows
    municipalities = df[~df.index.str.contains('sub-regional unit|WHOLE COUNTRY|HE 15/2017 vp|Uusimaa|Ostrobothnia|Åland')]

    # Further subset the rows that have proportion of Swedish speaking people and proportion of foreigners both above 5%
    subset = municipalities[
        (municipalities['Share of Swedish-speakers of the population, %'] > 5) &
        (municipalities['Share of foreign citizens of the population, %'] > 5)
    ]
    
    # Take only columns about population, the proportions of Swedish speaking people and foreigners
    final_df = subset[[
        'Population', 
        'Share of Swedish-speakers of the population, %', 
        'Share of foreign citizens of the population, %'
    ]]
    
    return final_df

def main():
    result_df = swedish_and_foreigners()
    
    print("Final DataFrame:")
    print(result_df)
    
    correlation = result_df.corr()
    print("\nCorrelation Matrix:")
    print(correlation)

if __name__ == "__main__":
    main()

