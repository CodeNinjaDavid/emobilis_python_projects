marks = int(input("Enter students score: "))
if marks > 80 and marks <= 100:
    print("You scored an A")
elif marks > 70 and marks <=79:
    print("You scored a B")
elif marks > 50 and marks <=69:
    print("You scored a C")
elif marks > 30 and marks <=59:
    print("You Scored a D")
elif marks > 1 and marks <=29:
    print("You Failed!!")


#create a python program to check if a given yyear is a leap year
#the year is divisible by 4 but not divisible by 100 except if its also divisible by 400

 is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Test the function
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
