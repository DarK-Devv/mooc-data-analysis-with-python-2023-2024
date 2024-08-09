#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data(file_path='src/mystery_data.tsv'):
    data = pd.read_csv(file_path, sep='\t')
    
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    
    model = LinearRegression(fit_intercept=False).fit(X, y)
    
    coefficients = model.coef_
    
    return coefficients

def main():
    coefficients = mystery_data()
    
    for i, coef in enumerate(coefficients, start=1):
        print(f"Coefficient of X{i} is {coef}")

if __name__ == "__main__":
    main()
