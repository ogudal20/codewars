#!/usr/bin/python3

def get_count(sentence):
    vowels  = {'a': 0, 'e': 0, 'i':0, 'o': 0, 'u': 0}
    for chr in sentence:
        if chr in vowels.keys():
            vowels[chr] += 1

    return sum(vowels.values())


