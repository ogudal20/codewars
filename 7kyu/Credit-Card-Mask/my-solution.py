# return masked string
def maskify(cc):
    if len(cc) < 4:
        return cc
    new_string = ""
    mask = cc[0:-4]
    for char in mask:
        new_string += char.replace(char, '#')
    return new_string + cc[-4:]
