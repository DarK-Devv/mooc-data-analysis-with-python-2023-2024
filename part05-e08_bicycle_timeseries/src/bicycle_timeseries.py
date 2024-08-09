import pandas as pd

def bicycle_timeseries():
    # Read the data set
    file_path = 'src/Helsingin_pyorailijamaarat.csv'
    df = pd.read_csv(file_path, sep=';')
    
    # Clean the data: Drop columns and rows with all NaN values
    df = df.dropna(how='all', axis=0)
    df = df.dropna(how='all', axis=1)
    
    # Split the Päivämäärä column into separate components
    date_parts = df['Päivämäärä'].str.split(expand=True)
    date_parts.columns = ['Weekday', 'Day', 'Month', 'Year', 'Time']
    
    # Map Finnish month names to numbers
    months = {
        'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5,
        'kesä': 6, 'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12
    }
    date_parts['Month'] = date_parts['Month'].map(months)
    
    # Extract the hour component from the Time column
    date_parts['Hour'] = date_parts['Time'].str.split(':', expand=True)[0].astype(int)
    
    # Create a DatetimeIndex from the parsed components
    date_parts['Datetime'] = pd.to_datetime(date_parts[['Year', 'Month', 'Day', 'Hour']])
    
    # Set the DatetimeIndex as the index of the DataFrame
    df = df.drop(columns=['Päivämäärä'])
    df = df.set_index(date_parts['Datetime'])
    
    return df

def main():
    df = bicycle_timeseries()
    print(df.head())

if __name__ == "__main__":
    main()
