def square_digits(num):
    
    res = []
    for i in str(num):
        res.append((int(i)*int(i)))
    
    result = ''.join(str(x) for x in res)
    return int(result)
