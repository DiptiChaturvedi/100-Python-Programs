# . Check whether a year is a leap year

year = int(input("enter year:"))

if year % 400 == 0:
    print("this is leap year..")

elif year % 100 == 0:
    print("this is not  leap yearrr")

elif year % 4 == 0:
    print("this  is leap year")



else:
    print("this is not leap year")
