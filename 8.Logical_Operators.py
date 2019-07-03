'''
Author - Shreeyash Haritashya
Date - 29th June 2019
Description - Understanding logical operators in Python
'''
city = input("Where do you live : ")
city2 = input("Birth city : ")

# and, both condition must be true
if city == "jaipur" and city2 == "ajmer":
    print("You live in Rajasthan")
else:
    print("You live somewhere else")

# or, any one condition must be true
if city == "jaipur" or city == "ajmer":
    print("You live somewhere in Rajasthan")
else:
    print("You live somewhere else") 

# not, it negates the true or false value..
'''
2-8 and 65 above - free entry
10 dollars for everyone else
'''
age = int(input("Enter your age : "))

if not ((age >= 2 and age <= 8) or age >= 65):
    print("You will pay 10 dollars and are not a child or senior!")
else:
    print("You are a child or a senior, your entry is free") 

