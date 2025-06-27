import string
import random
Characters=string.ascii_letters +string.digits + string.punctuation # the ascii genetares you both random uppercase and lowercase letters and the strin.digits generate numbers wwhiles the string.punctuation generates you special characters

def password_generator(length=12,by_numbers=True,by_special_charc=True): #function
    password="".join(random.choice(Characters)for i in range(12))
    return password

option=input("Do you want to generate a passowrd? (Yes/No) : ")

# using control flow
if option=="Yes":
    password_generator()  #ivoke the fuction 
elif option=="No":
    print("Program ended") 
else:
    print("Invalid input, please enter(Yes/No)")       




