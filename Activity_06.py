my_list = input().split()
new_list = my_list[0:3]
print(my_list)
print(new_list)
my_list[0] = 0
new_list[0] = 0
my_list[-1] = 0
new_list[-1] = 0
print(my_list)
print(new_list)