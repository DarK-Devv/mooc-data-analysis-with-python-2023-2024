#!/usr/bin/env python3

import pandas as pd

def last_week():
    # Path to the TSV file
    file_path = 'src/UK-top40-1964-1-2.tsv'
    
    # Read the dataset with the correct delimiter
    df = pd.read_csv(file_path, delimiter='\t')
    
    # Convert 'New' and 'Re' to missing values (None/NaN)
    df['LW'] = df['LW'].replace({'New': None, 'Re': None})
    
    # Convert 'LW' to numeric, forcing errors to NaN
    df['LW'] = pd.to_numeric(df['LW'], errors='coerce')
    
    # Create a DataFrame for last week's top 40
    last_week_df = pd.DataFrame(columns=df.columns)
    
    # Find entries that were on last week's list (LW column not null)
    last_week_entries = df.dropna(subset=['LW'])
    
    # Copy entries to last week's DataFrame
    last_week_df = last_week_df.append(last_week_entries)
    
    # Rename 'Pos' to 'Last Week Pos' and 'LW' to 'Pos'
    last_week_df.rename(columns={'Pos': 'Last Week Pos', 'LW': 'Pos'}, inplace=True)
    
    # Set 'Last Week Pos' as index to correctly fill missing values later
    last_week_df.set_index('Pos', inplace=True)
    
    # Ensure the index is sorted by 'Pos'
    last_week_df = last_week_df.sort_index()
    
    # Handle songs that are new or re-entries
    new_entries = df[df['LW'].isnull()]
    
    # Create a new DataFrame for new/re entries
    new_entries_df = pd.DataFrame(columns=df.columns)
    
    # Fill the new entries DataFrame with the appropriate values
    new_entries_df['Pos'] = new_entries['Pos']
    new_entries_df['Title'] = new_entries['Title']
    new_entries_df['Artist'] = new_entries['Artist']
    new_entries_df['Publisher'] = new_entries['Publisher']
    new_entries_df['Peak Pos'] = new_entries['Peak Pos']
    new_entries_df['WoC'] = new_entries['WoC']
    
    # Set 'Pos' as index
    new_entries_df.set_index('Pos', inplace=True)
    
    # Combine the two DataFrames
    combined_df = pd.concat([last_week_df, new_entries_df])
    
    # Fill missing values in the combined DataFrame
    combined_df = combined_df.reindex(range(1, 41)).sort_index()
    
    return combined_df.reset_index()

def main():
    df = last_week()
    print(df)

if __name__ == "__main__":
    main()
