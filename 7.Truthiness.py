'''
Author - Shreeyash Haritashya
Date - 29th June 2019
Description - Understanding truthiness and falsiness in Python
'''

animal = input("enter your favorite animal : ")

if animal: #checks wether a string is empty or not, if true(truthiness, i.e not empty)
    print(animal + " is my favourite too!")
else:
    print("You didn't say anything!")    