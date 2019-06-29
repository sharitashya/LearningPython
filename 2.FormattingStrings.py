'''
Author - Shreeyash Haritashya
Date - 29th June 2019
Description - Formatting Strings, using String interpolation
'''


#using f strings
x = 10
formatted = f"Your guess of {8} was incorrect!"
print(formatted)

#performing math inside {}
formatted = f"Your guess of {8 + 10} was incorrect!"
print(formatted)



#using .format method (Python 2 -> 3.5)
y = 15
formatted = "I've told you {} times already!".format(y)
print(formatted)



#the old way => % operator (deprecated)
z = 20
formatted = "I've told you %d times already!" % (z)
print(formatted)