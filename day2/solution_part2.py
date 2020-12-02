import os

input_file = os.path.join(os.getcwd(), "day1/input.txt")

nb_valid_passwords = 0


def is_valid_password(position1, position2, special_letter, password):
    position1 -= 1
    position2 -= 1
    if special_letter == password[position1] and special_letter != password[position2]:
        return True
    elif (
        special_letter != password[position1] and special_letter == password[position2]
    ):
        return True
    elif (
        special_letter != password[position1] and special_letter != password[position2]
    ):
        return False
    elif (
        special_letter == password[position1] and special_letter == password[position2]
    ):
        return False
    else:
        return False


with open("day2/input.txt", "r") as f:
    for line in f.readlines():
        # print(line)
        [numbers, letter, password] = line.split(" ")
        [position1, position2] = numbers.split("-")
        letter = letter[0]
        print(position1, position2)
        print(letter)
        print(password)
        print(is_valid_password(int(position1), int(position2), letter, password))
        if is_valid_password(
            int(position1), int(position2), letter, password
        ):
            nb_valid_passwords += 1

print(f"The number of valid passwords is: {nb_valid_passwords}")
