def accum(s):
    # your code
    return '-'.join(chr.capitalize() + chr.lower() * i for i, chr in enumerate(s))
