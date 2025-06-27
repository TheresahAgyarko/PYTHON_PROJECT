import string 
import random    
character=string.ascii_letters + string.digits + string.punctuation

def password_generator(length=12,By_numbers=True,By_special_charac=True):
    password="".join(random.choice(character)for i in range(12))
    return password
option=input("Do you want to generate password(Yes/No) : ")

# using control flow
if option=="Yes":
    password_generator()    #ivoke ya function
elif option=="No":
    print("End program") 
else:
    print("Invalid input, please enter (Yes/No)") 
          





