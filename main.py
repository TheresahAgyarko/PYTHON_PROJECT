import random
import string
def create(length=10,by_nums=True,by_letters=True,by_special_charac=True):
    character=string.ascii_letters  #for both lower and upper case letters from A-Z
    #  using control structure
    if by_nums:
        character+=string.digits #thus generating characters plus numbers 
    if by_special_charac:
        character+=string.punctuation #thus adding characters to special characters to create a password
    else:
        return "Invalid"    
    password="".join(random.choice(character) for i in range(length))
    return password

