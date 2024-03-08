Input = ["anymore", "raven", "me", "communicate"] 

print(max(Input, key=len))  
print(min(Input, key=len))


s = "anymore", "raven", "me", "communicate"
count = 0
for letter in s:
    if letter == 'a':
        count += 1
print(count)
