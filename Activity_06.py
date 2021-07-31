my_list = input().split()
new_list = my_list[0:3]
print("sliced list = ", new_list)
my_list[0] = 0
new_list[0] = 0
my_list[-1] = 0
new_list[-1] = 0
print("replaced list-1 = ", my_list)
print("replaced list-2 = ",new_list)

# Oh My God ! 1
# sliced list =  ['Oh', 'My', 'God']
# replaced list-1 =  [0, 'My', 'God', '!', 0]
# replaced list-2 =  [0, 'My', 0]