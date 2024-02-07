#!/usr/bin/python3
user_age = input("What is your age in years?")
# Calculate age in days
age_in_days = int(user_age) * 365
print("Your %s in days is %s" % ("age", age_in_days))
# Calculate age in months
age_in_months = int(user_age) * 12
print("Your age in months is {}".format(age_in_months))
# Calculate age in hours
age_in_hours = age_in_days * 24
print(f"Your age in hours is {age_in_hours}")