import pandas as pd

def best_record_company():
    file_path = 'src/UK-top40-1964-1-2.tsv'
    df = pd.read_csv(file_path, sep='\t')
    
    publisher_woc_sum = df.groupby('Publisher')['WoC'].sum()
    
    best_publisher = publisher_woc_sum.idxmax()
    
    best_publisher_singles = df[df['Publisher'] == best_publisher]
    
    return best_publisher_singles

def main():
    df = best_record_company()
    print(df)

if __name__ == "__main__":
    main()
