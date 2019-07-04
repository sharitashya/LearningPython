'''
Author - Shreeyash Haritashya
Date - 4th July 2019
Description - Bouncer program, to check the age of the user.
'''

#ask for age
age = int(input("What's your age ? \n"))

# 18-21 wrist band
if (age >= 18 and age < 21):
    print("Your entry is allowed!!, with a wrist band. \nYou are not allowed to drink.")
# 21+ drink normal entry
elif (age >= 21):
    print("You can enter and can drink too!!")
# 18 below, too young sorry..
elif (age < 18):
    print("Sorry, too young to enter!!")
else:
    print("Invalid input!!")

    