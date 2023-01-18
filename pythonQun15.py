import random
import string

def random_pass(length):
    result_str = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    print("your randomly generated password :",result_str)
    
random_pass(length=int(input("Enter the length of password:")))
    
    