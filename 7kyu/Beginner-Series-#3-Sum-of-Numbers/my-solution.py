def get_sum(a,b):
    sum_num = 0
    if a == b:
        return a
    if a > b:
        for i in range(a, b-1, -1):
            sum_num += i
        return sum_num
    if b > a:
        for i in range(a, b+1 , 1):
            sum_num += i
        return sum_num
