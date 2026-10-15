# Swap two numbers — without a temporary variable

a = int(input("Enter num:"))
b = int(input("enter num:"))

print("before swapping value of a=",a)
print("before swapping value of b=",b)
temp = a
a = b
b = temp

print("after swapping value of a=",a)
print("after swapping value of b=",b)