import pandas as pd

def read_data(file_path, sep='\t'):
    return pd.read_csv(file_path, sep=sep)

def top_bands():
    uk_top40_path = 'src/UK-top40-1964-1-2.tsv'
    bands_path = 'src/bands.tsv'
    
    uk_top40 = read_data(uk_top40_path)
    bands = read_data(bands_path)

    uk_top40.columns = uk_top40.columns.str.strip()
    bands.columns = bands.columns.str.strip()
    uk_top40['Artist'] = uk_top40['Artist'].str.strip().str.lower()
    bands['Band'] = bands['Band'].str.strip().str.lower()

    merged_df = pd.merge(uk_top40, bands, left_on='Artist', right_on='Band', how='inner')
    
    return merged_df

def main():
    df = top_bands()
    print(df.shape)
    print(df.head())

if __name__ == "__main__":
    main()
