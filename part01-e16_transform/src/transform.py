#!/usr/bin/env python3

def transform(str1, str2):
    # Split the strings into words and convert them to integers
    list1 = list(map(int, str1.split()))
    list2 = list(map(int, str2.split()))
    
    # Use zip to combine the two lists element-wise and calculate the product
    result = [x * y for x, y in zip(list1, list2)]
    
    return result

# Example usage:
str1 = "1 5 3"
str2 = "2 6 -1"
result = transform(str1, str2)
print(result)  # Output: [2, 30, -3]
