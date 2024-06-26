import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("\n*** Welcome to Security Password Generator ***")

# Asking the user to input how many letters, numbers and symbols to generate in a password.

number_of_letters = int(input("\nHow many letters would you like in your password? \n"))
number_of_symbols = int(input("\nHow many symbols would you like in your password? \n"))
number_of_numbers = int(input("\nHow many numbers would you like in your password? \n"))

# Empty password
password = []

# For loop for letters is used to randomly generate numbers from 1 to the number of letters the user wants.
# Then use the random.choice() function to randomly generate the number of letters (strings) from the letters list.
# Once the number of letters is randomly generated, it passes the letters from variable generate_letter variale into an empty into a password variable which contains an empty list.
# Random.shuffle() function is where it re-organizes the letters, numbers and symbols in the list to make the password more complex.
# Then concactinate the strings within the list using .join() function and print the randomly generated password in letters.

for generate_letter in range(1, number_of_letters + 1):
    generate_letter = random.choice(letters)
    password += generate_letter
    random.shuffle(password)


for generate_symbols in range(1, number_of_symbols + 1):
    generate_symbols = random.choice(symbols)
    password += generate_symbols
    random.shuffle(password)

for generate_numbers in range(1, number_of_numbers + 1):
    generate_numbers = random.choice(numbers)
    password += generate_numbers
    random.shuffle(password)

# Then concactinate the strings within the list using .join() function after letters, numbers and symbols are randomly generated in a list

join_password = "".join(password)
print(f"\nGenerated Password: {join_password}\n")
