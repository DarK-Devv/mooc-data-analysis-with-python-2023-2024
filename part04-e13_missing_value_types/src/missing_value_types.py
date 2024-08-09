#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    # Create the DataFrame with the given data
    data = {
        "State": ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"],
        "Year of independence": [np.nan, 1917, 1776, 1523, np.nan, 1992],
        "President": [np.nan, "Niinistö", "Trump", np.nan, "Steinmeier", "Putin"]
    }
    
    df = pd.DataFrame(data)
    df.set_index("State", inplace=True)
    
    return df

def main():
    df = missing_value_types()
    print(df)

if __name__ == "__main__":
    main()
