def array_diff(a, b):
    hashset = set()
    result = []
    
    for i in b:
        hashset.add(i)
    
    for i in a:
        if i in hashset:
            continue
        result.append(i)
    return result
