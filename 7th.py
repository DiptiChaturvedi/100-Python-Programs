#  Calculate simple interest

principal = int(input("Enter principal:"))
rate = int(input("enter rate:"))
time = int(input("enter time:"))


SI = (principal * rate * time) / 100

print("Simple Interest is =",SI)