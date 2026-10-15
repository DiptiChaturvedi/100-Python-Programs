# Find the largest of three numbers
 
a = int(input("enter num1:"))
b = int(input("enter num2:"))
c = int(input("enter num3:"))

if a > b and c:
    print("num1 is largest")
elif b > a and c:
    print("num2 is largest")

else:
    print("num3 is largest")