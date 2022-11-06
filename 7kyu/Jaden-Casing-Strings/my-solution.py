def to_jaden_case(string):

    new_string = string.split(" ")
    result = []
    for chr in new_string:
        result.append(chr.capitalize())
        
    return ' '.join(result)
