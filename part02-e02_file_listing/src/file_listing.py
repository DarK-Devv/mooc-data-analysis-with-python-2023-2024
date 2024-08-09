#!/usr/bin/env python3

import re

def file_listing(filename="src/listing.txt"):
    result = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Use regular expression to extract relevant fields
            match = re.match(r'([^\s]+)\s+(\d+)\s+([^\s]+)\s+([^\s]+)\s+(\d+)\s+([A-Za-z]+)\s+(\d+)\s+(\d+):(\d+)\s+(.+)', line)
            
            if match:
                size = int(match.group(5))
                month = match.group(6)
                day = int(match.group(7))
                hour = int(match.group(8))
                minute = int(match.group(9))
                filename = match.group(10)
                
                result.append((size, month, day, hour, minute, filename))
    
    return result

def main():
    result = file_listing()
    for item in result:
        print(item)

if __name__ == "__main__":
    main()

