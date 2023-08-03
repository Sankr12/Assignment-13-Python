''' Write a python script to change the values "SQL" and "ReactNative" with the values "NoSQL" and "Flutter" 
(list of this list = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]) '''

import copy
print()
My_list = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
Oldlist = copy.copy(My_list)

My_list[3] = "Flutter"
My_list[1] = "NoSQL"

print("Old List:",Oldlist)
print()
print("New List:",My_list)

print()
