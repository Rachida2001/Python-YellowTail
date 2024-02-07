# Prompt the user to input their age in years
#!/usr/bin/python3
age_years = int(input("Enter your age in years: "))

# Calculate age in terms of days, months, and hours
age_days = age_years * 365
age_months = age_years * 12
age_hours = age_days * 24

# Print the age in terms of days, months, and hours
print("Your age in terms of:")
print("Days: " + str(age_days))
print("Months: " + str(age_months))
print("Hours: " + str(age_hours))
