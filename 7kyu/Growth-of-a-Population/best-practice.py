def nb_year(p0, percent, aug, p):
    t = 0
    while p0 < p:
        p0 = int(p0*(1 + percent/100)) + aug  # my mathematical brain hates that I need to round this
        t += 1
    return t
