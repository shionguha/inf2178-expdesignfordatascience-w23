#enter participants in years
age = float(input("enter age in years:"))

# Display status
print("Status is", age)
if age >= 18:
    print("Adult")
elif age >=10:
    print("Teenger")
elif age < 10:
    print("Nonage")
