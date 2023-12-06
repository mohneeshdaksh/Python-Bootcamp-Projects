#Consufed in finding which year is a leap year? 
#No worries! Just type the year and I'll let you know whether it is a leap year or not!
print("Leap Year Finder!")
year = int(input("Please provide the year - "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year!")
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")