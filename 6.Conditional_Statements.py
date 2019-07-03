'''
Author - Shreeyash Haritashya
Date - 29th June 2019
Description - Understanding conditional statements in Python
'''

name = input("Enter the author name : ")
if name == "Shreeyash": #colon is essential, it signifies that there will be an indentation block.
    print("Valar Morghulis")
elif name == "Haritashya":
    print("That's my surname")
	# you can have multiple elif.... if you want!
else: 
    print("Carry on!")        
