year = int(input("Enter a year: "))
if year %4==0 and (year % 100 != 0 or year % 400 == 0):
    print("This is a leap year")
else:
    print("this is not a leap year")

    #write a progam to calculate a the ticket price of a movie

    0-5 years - free
    6-12 years -500
    13-17 years- 1000
    18+ years- 1500