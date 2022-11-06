def find_short(s):
    s = s.split()
    sum = float('inf')
    for char in s:
        if len(char) < sum:
            sum = len(char)
    return sum

