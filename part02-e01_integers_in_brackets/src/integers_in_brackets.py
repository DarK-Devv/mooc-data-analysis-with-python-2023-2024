#!/usr/bin/env python3


import re

def integers_in_brackets(input_str):
    # Use regular expression to find integers within brackets
    pattern = r'\[\s*([-+]?\d+)\s*\]'
    matches = re.findall(pattern, input_str)
    
    # Convert the matched strings to integers and return them
    return [int(match) for match in matches]


