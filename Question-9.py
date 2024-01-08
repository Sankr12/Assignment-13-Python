# Write a python script to create a list of city names taken from the user.

print()
num=int(input("Enter the city number you want to enter: "))
print("Enter city names: ")
city_name = []

while num:
    citynames = input()
    city_name.append(citynames)
    num-=1

print()
print("List of city names:",city_name)
print()