#!/usr/bin/env python3
def file_extensions(filename):
    no_extension_files = []
    extension_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '.' in line and line.rfind('.') != 0:
                name, ext = line.rsplit('.', 1)
                if ext in extension_dict:
                    extension_dict[ext].append(line)
                else:
                    extension_dict[ext] = [line]
            else:
                no_extension_files.append(line)
    
    return no_extension_files, extension_dict

def main():
    filename = 'src/filenames.txt'  # Path to the input file
    no_ext_files, ext_dict = file_extensions(filename)
    
    # Print number of files with no extension
    print(f"{len(no_ext_files)} files with no extension")
    
    # Print each extension and the number of files with that extension
    for ext in sorted(ext_dict):
        print(f"{ext} {len(ext_dict[ext])}")

if __name__ == '__main__':
    main()
