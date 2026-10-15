#  Calculate compound interest


principal = int(input("enter principal: "))
rate = int(input("enter rate:"))
time = int(input("enter time:"))

total_amount = principal*(1 + rate/100)**time
CI = total_amount - principal

print("compound interest is", CI)
