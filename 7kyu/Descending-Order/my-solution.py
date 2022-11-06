def descending_order(num):
    res = []
    for i in str(num):
        res.append(int(i))
    
    res = sorted(res, reverse=True)
    return int(''.join(str(x) for x in res))
