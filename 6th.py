#  Convert Celsius to Fahrenheit and Fahrenheit to Celsius


celsius_input = int(input("enter temperature in celsius:"))
fahrenheit  = (celsius_input * 9/5) + 32

fahrenheit_input = int(input("enter temperature in fahrenheit:"))
celsius_result  = (fahrenheit_input - 32) * 5/9


print("Celsius =", celsius_result)
print("Fahrenfeit =", fahrenheit_input)