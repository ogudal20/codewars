def longest(a1, a2):
    hash_a1 = {}
    for char1 in a1:
        hash_a1[char1] = 1 + hash_a1.get(char1, 0) 
    for char2 in a2:
        hash_a1[char2] = 1 + hash_a1.get(char2, 0)
    return ''.join(sorted(hash_a1.keys()))
