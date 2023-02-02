import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

# Compare the numbers to eachother 
if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number2 > number1:
    print(f"{number2} is greater than {number1}")    
else:
    print(f"{number1} equals to {number2}")