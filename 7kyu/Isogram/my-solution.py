def is_isogram(string):
    hashset = set()
    
    for char in string.lower():
        if char in hashset:
            return False
        hashset.add(char)
    return True
