def find_it(seq):
    hashmap = {}
    
    for i in seq:
        hashmap[i] = 1 + hashmap.get(i, 0)
    
    for count, value in hashmap.items():
        if value % 2 != 0:
            return count
          

