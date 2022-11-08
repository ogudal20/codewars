def nb_year(p0, percent, aug, p):
    num_of_years = 0
    percent = percent/100
    while p0 < p:
        sum = p0 * percent
        p0 = int(sum + aug + p0)
        num_of_years += 1
    return num_of_years
        
