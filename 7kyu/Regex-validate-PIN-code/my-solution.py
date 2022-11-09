import re
def validate_pin(pin):
    if re.findall('[a-z-.+\s/:]', pin):
        return False
    if len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False
  
