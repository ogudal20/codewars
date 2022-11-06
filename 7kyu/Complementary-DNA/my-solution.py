def DNA_strand(dna):

    new_string = ""
    for char in dna:
        print(char)
        if char == 'A':
            char = char.replace(char, 'T')
            new_string += char
        elif char == 'T':
            char = char.replace(char, 'A')
            new_string += char
        elif char == 'C':
            char = char.replace(char, 'G')
            new_string += char
        elif char == 'G':
            char = char.replace(char, 'C')
            new_string += char
        
            
    return new_string
