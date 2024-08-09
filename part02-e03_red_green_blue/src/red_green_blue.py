#!/usr/bin/env python3
import re

def red_green_blue():
    cleaned_lines = []
    with open('src/rgb.txt', 'r') as file:
        # Skip the first line
        file.readline()
        
        for line in file:
            # Strip leading and trailing whitespace
            line = line.strip()
            # Use regex to find all parts (numbers and color name)
            parts = re.findall(r'\S+', line)
            # Join parts with a single tab character
            cleaned_line = '\t'.join(parts)
            # Ensure that the line has exactly four fields separated by a tab
            if len(parts) > 4:
                parts = parts[:3] + [' '.join(parts[3:])]
                cleaned_line = '\t'.join(parts)
            cleaned_lines.append(cleaned_line)
    
    return cleaned_lines