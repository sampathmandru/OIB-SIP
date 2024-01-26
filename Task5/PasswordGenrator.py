#import random module
import random 

passwordlen = int (input("Enter the length of password : "))

s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ|@#$%&*"
#Ramdom sampling by joining the length of the password and the s variable

P = "".join(random.sample(s,passwordlen))

print(P)