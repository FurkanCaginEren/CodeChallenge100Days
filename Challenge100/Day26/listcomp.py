# List Compharison


number = [1,2,3]
# new_list = []

# for n in number:
#     add_1 = n+1
#     new_list.append(add_1)

# new_list = [new_item for item in list]

new_list  = [n+1 for n in number]

# print(new_list)

name = "angela"

letter_list = [letter for letter in name]

# print(letter_list)


challange_list =[n*2 for n in range(1,5)]

# print(challange_list)

names = ["alex","beth","caroline","Eleanor","dave","freddie"]

short_names = [name for name in names if len(name) < 5]

print(short_names)

long_upper_names = [n.upper() for n in names if len(n) > 4]

print(long_upper_names)