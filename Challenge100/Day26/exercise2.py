### Check 2 txt files then check if same numbers and add into a list


with open("Day26/file1.txt") as list1:
    data1 = list1.readlines()
    

with open("Day26/file2.txt") as list2:
    data2 = list2.readlines()
    

common_data = [int(n) for n in data1 if n in data2],

print(common_data)