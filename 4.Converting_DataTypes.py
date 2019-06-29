'''
Author - Shreeyash Haritashya
Date - 29th June 2019
Description - Understanding Datatype Conversion
'''

#int function just chops off, all the decimals.
decimal = 12.2345234623564
integer = int(decimal)
print(integer)
print(type(integer))

my_list = [1, 2, 3]
my_list_as_a_string = str(my_list) #"[1, 2, 3]"
print(my_list_as_a_string)
print(type(my_list_as_a_string))