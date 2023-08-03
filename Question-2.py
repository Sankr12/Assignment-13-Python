# Write a python script to get the data type of a list.

print()
my_list = [1,3+4j,True,5.4,"Sandeep",4]

for i in my_list:
    data_type = type(i)
    print("Data type of",i,":",data_type)

print()