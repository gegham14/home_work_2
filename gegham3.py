# import re
# password = "R@m@_f0rtu9e$"
# flag = 0
# while True:
#     if (len(password)<=8):
#         flag = -1
#         break
#     elif not re.search("[a-z]", password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]" , password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break
 
# if flag == -1:
#     print("Not a Valid Password ")


import re


def validate_password(password):  
    if len(password) < 8:  
        return False  
    if not re.search("[a-z]", password):  
        return False  
    if not re.search("[A-Z]", password):  
        return False  
    if not re.search("[0-9]", password):  
        return False  
    return True  
  
password = "P@ssw0rd"  
if validate_password(password):  
    print("Valid password")  
else:  
    print("Invalid password") 