'''
Author - Shreeyash Haritashya
Date - 29th June 2019
Description - Simple application to convert k.m to miles
'''

print("How many kilometers did you cycle today ?")
kms = float(input())
miles = kms/1.60934
miles = round(miles, 4) #round(things to round, how many decimal points )
print(f"Okay, Your {kms}km ride was {miles}mi")