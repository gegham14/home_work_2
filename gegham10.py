# l = {1: 1, 2:4, 3:9, 4:16, 5:25}
# l=int(input("100: "))
# d = dict()
# for x in range(1,l+1):
#     d[x]=x**2
# print(d)


def generate_dict(number):
    return {i:i**2 for i in range(1,number+1)}

print(generate_dict(5))
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}