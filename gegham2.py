# s=[10,11,12,9,10,11]
# length = len(s)-1
# for i in range(length):
#     if s[i] > s[i + 1]:
#         s[i], s[i + 1] = s[i + 1], s[i]
# print(s[-1])


# list = [2,3,5,8,12,15]
# def find_max(list):
#         max = list[0]
#         for number in list:
#             if (number > max):
#                 max = number
#             return max



l = [2,5,80,23,46,9,8,122,574,85]
l.sort()
print(l)
print("max in list", l[-1])