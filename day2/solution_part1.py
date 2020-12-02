import os

input_file = os.path.join(os.getcwd(), "day1/input.txt")

nb_valid_passwords = 0


def is_valid_password(min_occurences, max_occurrences, special_letter, password):
    nb_occurences = 0
    for letter in password:
        if letter == special_letter:
            nb_occurences += 1
    
    return min_occurences <= nb_occurences <= max_occurrences


with open("day2/input.txt", "r") as f:
    for line in f.readlines():
        print(line)
        [numbers, letter, password] = line.split(" ")
        [min_occurences, max_occurences] = numbers.split("-")
        letter = letter[0]
        print(min_occurences, max_occurences)
        print(letter)
        print(password)
        if is_valid_password(int(min_occurences), int(max_occurences), letter, password):
            nb_valid_passwords += 1

print(f"The number of valid passwords is: {nb_valid_passwords}")
