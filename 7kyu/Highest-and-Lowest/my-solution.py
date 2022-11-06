def high_and_low(numbers):
    num_list = []
    for i in (numbers.split()):
        num_list.append(int(i))
        
    nums_list = num_list.sort()
    
    return str(num_list[-1]) + ' ' + str(num_list[0])
