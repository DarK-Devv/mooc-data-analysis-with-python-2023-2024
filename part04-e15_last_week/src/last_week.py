import pandas as pd

def last_week():
    # Path to the TSV file
    file_path = 'src/UK-top40-1964-1-2.tsv'
    
    # Read the dataset with the correct delimiter
    df = pd.read_csv(file_path, delimiter='\t')
    
    # Convert 'New' and 'Re' to missing values (None/NaN)
    df['LW'] = df['LW'].replace({'New': pd.NA, 'Re': pd.NA})
    
    # Convert 'LW' to numeric, forcing errors to NaN
    df['LW'] = pd.to_numeric(df['LW'], errors='coerce')
    
    # Identify songs that were on last week's list
    last_week_df = df.dropna(subset=['LW']).copy()
    
    # Rename 'Pos' to 'Current Pos' and 'LW' to 'Pos' for last week's DataFrame
    last_week_df.rename(columns={'Pos': 'Current Pos', 'LW': 'Pos'}, inplace=True)
    
    # Adjust 'WoC' (Weeks on Chart)
    last_week_df['WoC'] = last_week_df['WoC'] - 1
    
    # Create a DataFrame with positions 1 to 40
    all_positions = pd.DataFrame({'Pos': range(1, 41)})
    
    # Merge last week's entries with all positions
    combined_df = pd.merge(all_positions, last_week_df, on='Pos', how='left')
    
    # Ensure missing values are correctly handled
    combined_df[['Title', 'Artist', 'Publisher', 'WoC']] = combined_df[['Title', 'Artist', 'Publisher', 'WoC']].fillna(pd.NA)
    
    # Handle Peak Pos column: set to NaN if the song was not present in the previous week
    combined_df['Peak Pos'] = combined_df['Peak Pos'].combine_first(df.set_index('Pos')['Peak Pos']).where(combined_df['Current Pos'].notna(), pd.NA)
    
    # Ensure LW column is present with NaNs where not applicable
    combined_df['LW'] = pd.NA
    
    return combined_df

def main():
    df = last_week()
    print(df)

if __name__ == "__main__":
    main()
