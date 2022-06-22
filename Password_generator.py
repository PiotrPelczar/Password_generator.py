import sys
import random
import string

Password = []
import sys

password_length = int(input("How long would you like your password to be? "))
characters_left = -1



if password_length < 5:
    print("Password need to have at least 5 characters. Try again")
    sys.exit(0)
else:
    characters_left = password_length


lowercase_letters = int(input("How many lower cases letters would you like to have in your password? "))
if lowercase_letters > characters_left:
    print("Not enough characters left in the password")
    sys.exit(0)
elif lowercase_letters < 0:
    print("The number of those characters can't be less than 0")
    sys.exit(0)
characters_left = characters_left - lowercase_letters
print("Characters left: ", characters_left)

uppercasse_letters = int(input("How many upper case letters would you like to have in your password? "))
if uppercasse_letters > characters_left:
    print("Not enough characters left in the password")
    sys.exit(0)
elif uppercasse_letters < 0:
    print("The number of those characters can't be less than 0")
    sys.exit(0)
characters_left = characters_left - uppercasse_letters
print("Characters left: ", characters_left)

special_characters = int(input("How many special characters would you like to have in your password? "))
if special_characters > characters_left:
    print("Not enough characters left in the password")
    sys.exit(0)
elif special_characters < 0:
    print("The number of those characters can't be less than 0")
    sys.exit(0)
characters_left = characters_left - special_characters
print("Characters left: ", characters_left)

digits = int(input("How many digits would you like to have in your password? "))
if digits > characters_left:
    print("Not enough characters left in the password")
    sys.exit(0)

elif digits < 0:
    print("The number of those characters can't be less than 0")
    sys.exit(0)
characters_left = characters_left - digits
print("Characters left: ", characters_left)


if characters_left > 0:
    print("The remaining characters will be filled with small letters")
    lowercase_letters += characters_left

print()
print("Password length:", password_length)
print("Upper letters: ", uppercasse_letters)
print("Small case letters: ", lowercase_letters)
print("Special characters: ", special_characters)
print("Digits: ", digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        Password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercasse_letters > 0:
        Password.append(random.choice(string.ascii_uppercase))
        uppercasse_letters -= 1
    if special_characters > 0:
        Password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        Password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(Password)

"".join(Password)

print("Your password is: ", "".join(Password))