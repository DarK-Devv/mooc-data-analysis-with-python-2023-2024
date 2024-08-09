import pandas as pd

def subsetting_with_loc(file_path='src/municipal.tsv'):
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
    
    # Use loc to subset the DataFrame from Akaa to Äänekoski and restrict to specific columns
    subset = df.loc['Akaa':'Äänekoski', [
        'Population', 
        'Share of Swedish-speakers of the population, %', 
        'Share of foreign citizens of the population, %'
    ]]
    return subset

def main():
    # Get the subset from Akaa to Äänekoski
    file_path = 'src/municipal.tsv'
    subset_df = subsetting_with_loc(file_path)
    
    # Print the result
    print("Subset from Akaa to Äänekoski:")
    print(subset_df)

if __name__ == "__main__":
    main()
