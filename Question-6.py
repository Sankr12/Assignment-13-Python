''' Write a python program to append elements from another list to the first list.
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]'''

print()
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

firstlist.append(secondlist[0])
firstlist.append(secondlist[1])
firstlist.append(secondlist[2])

print(firstlist)
print()