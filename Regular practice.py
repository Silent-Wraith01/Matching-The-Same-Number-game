number1 = int(input("Please enter a number"))
number2 = int(input("Please enter a number"))


while number1 != number2: 
    print(f"{number1} is not equal to {number2}")
    number1 = int(input("Please enter a number"))
    number2 = int(input("Please enter a number"))
print(f"{number1} is equal to {number2}")