def xo(s):
    count_x = {}
    count_o = {}
    
    for char in s.lower():
        if char == 'x':
            count_x[char] = 1 + count_x.get(char, 0)
        if char == 'o':
            count_o[char] = 1 + count_o.get(char, 0)
    
    return sum(count_x.values()) == sum(count_o.values())
