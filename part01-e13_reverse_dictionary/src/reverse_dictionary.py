#!/usr/bin/env python3

def reverse_dictionary(d):
    reversed_dict = {}
    
    for english_word, finnish_words in d.items():
        for finnish_word in finnish_words:
            if finnish_word not in reversed_dict:
                reversed_dict[finnish_word] = [english_word]
            else:
                reversed_dict[finnish_word].append(english_word)
    
    return reversed_dict

def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reversed_dict = reverse_dictionary(d)
    print(reversed_dict)

if __name__ == "__main__":
    main()

