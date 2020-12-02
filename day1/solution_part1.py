import os

input_file = os.path.join(os.getcwd(), "day1/input.txt")
MAGIC_NUMBER = 2020
ANSWER = 0
has_solution = False
first_number = 0
second_number = 0


numbers = []

with open(input_file, "r") as f:
    numbers = f.readlines()

# print(numbers, len(numbers))

for i1, number1 in enumerate(numbers):
    for i2, number2 in enumerate(numbers):
        # print(i1, i2)
        # print("-------------")
        # print()
        # print(f"Num1: {int(number1)}")
        # print(f"Num2: {int(number2)}")
        # print(f"The sum is: {int(number1) + int(number2)}")
        # print()
        if int(number1) + int(number2) == MAGIC_NUMBER:
            has_solution = True
            first_number = int(number1)
            second_number = int(number2)
            ANSWER = first_number * second_number
            break
    if has_solution:
        break
        

if has_solution:
    print(f"The numbers are: {first_number} and {second_number}")
    print(f"The answer is: {ANSWER}")
