import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import binom

# Step 1: Data Collection
def download_and_load_data(file_path):
    # Load data from the saved txt file
    df = pd.read_csv(file_path, sep=",")
    print("Columns in the DataFrame:", df.columns)
    return df

# Step 2: Data Cleaning
def clean_data(df):
    # Remove rows with invalid coordinates
    df = df[(df['LAT'] != 0) & (df['LONG'] != 0)]
    
    # Remove rows with unspecified species
    df = df[~df['SPECIES'].isin(['sp.', 'indet.'])]
    
    return df

# Step 3: Assign Time Units
def assign_time_units(df):
    mn_time_units = [
        (23, 21.7, 'MN1'), (21.7, 19.5, 'MN2'), (19.5, 17.2, 'MN3'),
        (17.2, 16.4, 'MN4'), (16.4, 14.2, 'MN5'), (14.2, 12.85, 'MN6'),
        (12.85, 11.2, 'MN7-8'), (11.2, 9.9, 'MN9'), (9.9, 8.9, 'MN10'),
        (8.9, 7.6, 'MN11'), (7.6, 7.1, 'MN12'), (7.1, 5.3, 'MN13'),
        (5.3, 5, 'MN14'), (5, 3.55, 'MN15'), (3.55, 2.5, 'MN16'),
        (2.5, 1.9, 'MN17'), (1.9, 0.85, 'MQ18'), (0.85, 0.01, 'MQ19')
    ]
    
    def get_time_unit(row):
        mean_age = (row['MIN_AGE'] + row['MAX_AGE']) / 2
        for start, end, unit in mn_time_units:
            if start >= mean_age > end:
                return unit
        return 'pre-MN' if mean_age > 23 else 'post-MN'
    
    df['TIME_UNIT'] = df.apply(get_time_unit, axis=1)
    
    # Expert corrections
    df.loc[df['LIDNUM'] == 'Samos Main Bone Beds', 'TIME_UNIT'] = 'MN12'
    df.loc[df['LIDNUM'] == 'Can Llobateres I', 'TIME_UNIT'] = 'MN9'
    
    return df

# Step 4: Assign Unique Species IDs
def assign_species_ids(df):
    df['SPECIES_ID'] = df['GENUS'] + ' ' + df['SPECIES']
    df['SPECIES_ID'] = df['SPECIES_ID'].factorize()[0]
    return df

# Step 5: Remove Duplicate Species Occurrences
def remove_duplicates(df):
    df = df.drop_duplicates(subset=['LIDNUM', 'SPECIES_ID'])
    return df

# Step 6: Analyze Occurrences Over Time
def analyze_occurrences(df):
    occurrences = df.groupby('TIME_UNIT').size().reset_index(name='TOTAL_OCCURRENCES')
    first_occurrences = df.drop_duplicates('SPECIES_ID').groupby('TIME_UNIT').size().reset_index(name='FIRST_OCCURRENCES')
    
    merged = pd.merge(occurrences, first_occurrences, on='TIME_UNIT')
    merged['PROPORTION_FIRST_OCCURRENCES'] = merged['FIRST_OCCURRENCES'] / merged['TOTAL_OCCURRENCES']
    
    return merged

def plot_occurrences_over_time(occurrences):
    plt.figure(figsize=(10, 6))
    plt.plot(occurrences['TIME_UNIT'], occurrences['PROPORTION_FIRST_OCCURRENCES'], label='Proportion of First Occurrences')
    plt.plot(occurrences['TIME_UNIT'], occurrences['TOTAL_OCCURRENCES'], label='Total Occurrences')
    plt.xlabel('Time Unit')
    plt.ylabel('Proportion / Total Occurrences')
    plt.legend()
    plt.title('Proportion of First Occurrences Over Time')
    plt.show()

# Step 7: Geographic Patterns
def plot_geographic_distribution(df):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    
    for time_unit in df['TIME_UNIT'].unique():
        subset = df[df['TIME_UNIT'] == time_unit]
        plt.figure(figsize=(20, 10))
        world.plot(color='wheat', edgecolor='black')
        plt.scatter(subset['LONG'], subset['LAT'], s=subset['SPECIES_ID'], alpha=0.5)
        plt.title(f'Distribution of Localities in Time Unit {time_unit}')
        plt.show()

# Step 8: Sampling Analysis
def sampling_analysis(df):
    continents = df.groupby('CONTINENT').size().reset_index(name='SAMPLE_SIZE')
    continents['AVERAGE_OCCURRENCES'] = df.groupby('CONTINENT')['SPECIES_ID'].nunique().reset_index(name='UNIQUE_SPECIES')['UNIQUE_SPECIES']
    
    return continents

# Step 9: Logistic Regression
def logistic_regression(df):
    regression_data = []
    
    for locality in df['LIDNUM'].unique():
        locality_data = df[df['LIDNUM'] == locality]
        prev_time_unit = locality_data['TIME_UNIT'].iloc[0] - 1
        prev_data = df[df['TIME_UNIT'] == prev_time_unit]
        
        for _, row in locality_data.iterrows():
            num_occurrences = len(prev_data)
            first_occurrence = 1 if row['SPECIES_ID'] in prev_data['SPECIES_ID'].values else 0
            regression_data.append([num_occurrences, first_occurrence])
    
    regression_df = pd.DataFrame(regression_data, columns=['PREV_OCCURRENCES', 'FIRST_OCCURRENCE'])
    
    X = regression_df['PREV_OCCURRENCES']
    y = regression_df['FIRST_OCCURRENCE']
    
    X = sm.add_constant(X)
    model = sm.Logit(y, X)
    result = model.fit()
    
    return result

def plot_regression(result):
    coefficients = result.params
    x_vals = np.linspace(0, 100, 500)
    y_vals = 1 / (1 + np.exp(-(coefficients[0] + coefficients[1] * x_vals)))
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='Logistic Regression')
    plt.fill_between(x_vals, y_vals - 1.96 * np.sqrt(y_vals * (1 - y_vals) / len(x_vals)), 
                     y_vals + 1.96 * np.sqrt(y_vals * (1 - y_vals) / len(x_vals)), alpha=0.2)
    plt.xlabel('Number of Occurrences in Previous Time Unit')
    plt.ylabel('Proportion of First Occurrences')
    plt.legend()
    plt.title('Logistic Regression of First Occurrences')
    plt.show()

# Step 10: Statistical Significance
def calculate_significance(df, result):
    significance_results = []
    
    for locality in df['LIDNUM'].unique():
        locality_data = df[df['LIDNUM'] == locality]
        prev_time_unit = locality_data['TIME_UNIT'].iloc[0] - 1
        prev_data = df[df['TIME_UNIT'] == prev_time_unit]
        
        num_prev_occurrences = len(prev_data)
        expected_proportion = 1 / (1 + np.exp(-(result.params[0] + result.params[1] * num_prev_occurrences)))
        
        actual_first_occurrences = locality_data['SPECIES_ID'].nunique()
        p_value = binom.sf(actual_first_occurrences - 1, len(locality_data), expected_proportion)
        
        significance_results.append([locality, expected_proportion, actual_first_occurrences, p_value])
    
    significance_df = pd.DataFrame(significance_results, columns=['LOCALITY', 'EXPECTED_PROPORTION', 'ACTUAL_FIRST_OCCURRENCES', 'P_VALUE'])
    
    return significance_df

def plot_significance(df):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    
    for time_unit in df['TIME_UNIT'].unique():
        subset = df[df['TIME_UNIT'] == time_unit]
        plt.figure(figsize=(20, 10))
        world.plot(color='wheat', edgecolor='black')
        plt.scatter(subset['LONG'], subset['LAT'], c=subset['P_VALUE'], cmap='coolwarm', s=100, alpha=0.5)
        plt.colorbar(label='p-value')
        plt.title(f'Significance of First Occurrences in Time Unit {time_unit}')
        plt.show()

# Main Execution
if __name__ == "__main__":
    # Load data
    df = download_and_load_data('src/data.csv')
    
    # Renaming columns to remove potential leading/trailing spaces
    df.columns = df.columns.str.strip()
    
    # Clean data
    df = clean_data(df)
    
    # Assign time units
    df = assign_time_units(df)
    
    # Assign species IDs
    df = assign_species_ids(df)
    
    # Remove duplicates
    df = remove_duplicates(df)
    
    # Analyze occurrences over time
    occurrences = analyze_occurrences(df)
    plot_occurrences_over_time(occurrences)
    
    # Plot geographic distribution
    plot_geographic_distribution(df)
    
    # Sampling analysis
    sampling = sampling_analysis(df)
    print(sampling)
    
    # Logistic regression
    result = logistic_regression(df)
    plot_regression(result)
    
    # Calculate significance
    significance_df = calculate_significance(df, result)
    plot_significance(significance_df)
