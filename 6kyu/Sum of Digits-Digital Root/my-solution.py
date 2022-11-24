def digital_root(n):
    num = str(n)
    for i in list(num):
        total = sum(list(map(int, num)))
        if total < 10:
            return total
        num = str(total)
