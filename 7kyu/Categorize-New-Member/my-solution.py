def open_or_senior(data):
    
    res = []
    for member in range(len(data)):
        if data[member][0] >= 55 and data[member][1] > 7:
            res.append('Senior')
        else:
            res.append('Open')
    return res
