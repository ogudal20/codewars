import math
def is_square(n):
    if n < 0: return False
    res = math.sqrt(n)
    return False if res % 1 != 0.0 else True
