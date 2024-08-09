import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    return pd.read_csv(file_path, sep=';')

def clean_data(df):
    df = df.dropna(how='all', axis=0)
    df = df.dropna(how='all', axis=1)
    return df

def parse_date(df):
    days = {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}
    months = {'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5, 'kesä': 6, 'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12}
    
    date_parts = df['Päivämäärä'].str.split(expand=True)
    date_parts.columns = ['Weekday', 'Day', 'Month', 'Year', 'Time']
    date_parts['Weekday'] = date_parts['Weekday'].map(days)
    date_parts['Month'] = date_parts['Month'].map(months)
    date_parts['Day'] = date_parts['Day'].astype(int)
    date_parts['Year'] = date_parts['Year'].astype(int)
    date_parts['Hour'] = date_parts['Time'].str.split(':', expand=True)[0].astype(int)
    
    return date_parts.drop(columns=['Time'])

def cyclists_per_day():
    file_path = 'src/Helsingin_pyorailijamaarat.csv'
    df = read_data(file_path)
    df = clean_data(df)
    
    date_parts = parse_date(df)
    
    df = df.drop(columns=['Päivämäärä'])
    df = pd.concat([date_parts, df], axis=1)
    
    # Drop the Weekday and Hour columns before grouping
    df = df.drop(columns=['Weekday', 'Hour'])
    
    grouped = df.groupby(['Year', 'Month', 'Day']).sum()
    
    return grouped

def main():
    df = cyclists_per_day()
    august_2017 = df.xs((2017, 8), level=('Year', 'Month'))

    plt.figure(figsize=(10, 6))
    august_2017.plot()

    plt.xlabel('Day in August 2017')
    plt.ylabel('Cyclists')
    plt.title('Cyclists per Day in August 2017')
    plt.xticks(range(1, 32))
    plt.grid(True)
    plt.legend(loc='upper right', fontsize='small')
    plt.show()

if __name__ == "__main__":
    main()
