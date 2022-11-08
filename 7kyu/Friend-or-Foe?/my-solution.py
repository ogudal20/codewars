def friend(x):
    res = []
    for name in x:
        if len(name) == 4:
            res.append(name)
    return res
