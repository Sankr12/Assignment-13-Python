''' Write a python program to append elements from another list to the first list.
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]'''

print()
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

for items in secondlist:
    firstlist.append(items)
print(firstlist)
print()