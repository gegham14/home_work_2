# new_list = "216.008.094.196"
# new_list.remove(1)
# print(new_list )

# def remove_zeros_from_ip(ip_add):
#   new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])  
#   return new_ip_add 

# print(remove_zeros_from_ip("216.008.094.196"))



ip = input("enter ip address:")
ip2 =".".join(map(str, map(int,ip.split("."))))
print("ip addess is :",ip2)


