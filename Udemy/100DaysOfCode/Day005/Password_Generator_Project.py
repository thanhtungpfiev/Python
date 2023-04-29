#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# passwd = ""
# for letter in range(0, nr_letters):
#     passwd += letters[random.randint(0, len(letters) - 1)]

# for symbol in range(0, nr_symbols):
#     passwd += symbols[random.randint(0, len(symbols) - 1)]

# for number in range(0, nr_numbers):
#     passwd += numbers[random.randint(0, len(numbers) - 1)]

# print(passwd)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passwd = ""
passwd_length = nr_letters + nr_numbers + nr_symbols
total_list = letters + numbers + symbols
nr_letter = 0
nr_symbol = 0
nr_number = 0
for i in range(0, passwd_length):
    c = total_list[random.randint(0, len(total_list) - 1)]
    if c in letters:
        if nr_letter < nr_letters:
            passwd += c
            nr_letter += 1
        else:
            if nr_symbol < nr_symbols:
                c = symbols[random.randint(0, len(symbols) - 1)]
                passwd += c
                nr_symbol += 1
            else:
                c = numbers[random.randint(0, len(numbers) - 1)]
                passwd += c
                nr_number += 1
    elif c in symbols:
        if nr_symbol < nr_symbols:
            passwd += c
            nr_symbol += 1
        else:
            if nr_letter < nr_letters:
                c = letters[random.randint(0, len(letters) - 1)]
                passwd += c
                nr_letter += 14
            else:
                c = numbers[random.randint(0, len(numbers) - 1)]
                passwd += c
                nr_number += 1
    else:
        if nr_number < nr_numbers:
            passwd += c
            nr_number += 1
        else:
            if nr_letter < nr_letters:
                c = letters[random.randint(0, len(letters) - 1)]
                passwd += c
                nr_letter += 1
            else:
                c = symbols[random.randint(0, len(symbols) - 1)]
                passwd += c
                nr_symbol += 1

print(passwd)
