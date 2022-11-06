import re
def disemvowel(string_):
    
    text = re.sub("[aeiouAEIOU]",'' ,string_)
    
    return text
 

