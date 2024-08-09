#!/usr/bin/env python3

import pandas as pd

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
    date_parts['Weekday'] = date_parts['Weekday'].map(days).astype(object)
    date_parts['Month'] = date_parts['Month'].map(months).astype(int)
    date_parts['Day'] = date_parts['Day'].astype(int)
    date_parts['Year'] = date_parts['Year'].astype(int)
    date_parts['Hour'] = date_parts['Time'].str.split(':', expand=True)[0].astype(int)
    
    return date_parts.drop(columns=['Time'])

def split_date_continues():
    file_path = 'src/Helsingin_pyorailijamaarat.csv'
    df = read_data(file_path)
    df = clean_data(df)
    
    date_parts = parse_date(df)
    
    df = df.drop(columns=['Päivämäärä'])
    df = pd.concat([date_parts, df], axis=1)
    
    return df

def cycling_weather():
    cycling_data = split_date_continues()
    weather_data = pd.read_csv('src/kumpula-weather-2017.csv')

    merged_data = pd.merge(
        cycling_data,
        weather_data,
        left_on=['Year', 'Month', 'Day'],
        right_on=['Year', 'm', 'd']
    )

    merged_data = merged_data.drop(columns=['m', 'd', 'Time', 'Time zone'])
    
    return merged_data

def main():
    df = cycling_weather()
    print(df.head())

if __name__ == "__main__":
    main()
