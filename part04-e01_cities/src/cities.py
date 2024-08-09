#!/usr/bin/env python3

import pandas as pd

def cities():
    data = {
        "City": ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"],
        "Population": [643272, 279044, 231853, 223027, 201810],
        "Total area": [715.48, 528.03, 689.59, 240.35, 3817.52]
    }
    
    df = pd.DataFrame(data)
    df.set_index("City", inplace=True)
    
    return df

def main():
    df = cities()
    print(df)

if __name__ == "__main__":
    main()
