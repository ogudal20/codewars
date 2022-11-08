import math
def find_next_square(sq):
    sqrt = math.sqrt(sq)
    if sqrt.is_integer() == False:
        return -1
    else:
        return int(sqrt + 1) ** 2

