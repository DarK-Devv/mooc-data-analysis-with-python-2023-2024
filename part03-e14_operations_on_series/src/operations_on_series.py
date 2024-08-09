#!/usr/bin/env python3


import pandas as pd

def create_series(list1, list2):
    if len(list1) != 3 or len(list2) != 3:
        raise ValueError("Both lists must have exactly 3 elements.")
    
    s1 = pd.Series(list1, index=['a', 'b', 'c'])
    s2 = pd.Series(list2, index=['a', 'b', 'c'])
    
    return s1, s2

def modify_series(s1, s2):
    # Add a new value to s1 with index 'd'
    s1['d'] = s2['b']
    
    # Delete the element from s2 with index 'b'
    del s2['b']
    
    return s1, s2

def main():
    # Example lists
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    
    # Create Series
    s1, s2 = create_series(list1, list2)
    
    # Modify Series
    s1, s2 = modify_series(s1, s2)
    
    # Print modified Series
    print("Modified Series s1:")
    print(s1)
    print("\nModified Series s2:")
    print(s2)
    
    # Add the modified Series
    result = s1 + s2
    print("\nResult of adding s1 and s2:")
    print(result)

# Run the main function to test the solution
if __name__ == "__main__":
    main()

