# Input = ["anymore", "raven", "me", "communicate"] 

# print(max(Input, key=len))  
# print(min(Input, key=len))


# s = "anymore", "raven", "me", "communicate"
# count = 0
# for letter in s:
#     if letter == 'a':
#         count += 1
# print(count)



ini_dict = { "a": 1, "b": 2, "c": 2 }
 
print("initial_dictionary", str(ini_dict))
 
flipped = {}
 
for key, value in ini_dict.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)
 
print("final_dictionary", str(flipped))