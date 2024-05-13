# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# * version 1
# with open("./Input/Names/invited_names.txt") as names_file:
#     names_list = names_file.readlines()
#     for index in range(len(names_list)):
#         with open("./Input/Letters/starting_letter.txt") as starting_letters_file:
#             letters_list = starting_letters_file.readlines()
#             names_list[index] = names_list[index].strip()
#             letters_list[0] = letters_list[0].replace("[name]", names_list[index])
#             with open(f"./Output/ReadyToSend/letter_for_{names_list[index]}.txt", mode="w") as send_letters_file:
#                 send_letters_file.write(''.join(letters_list))

# * version 2
with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letters_file:
    letter_contents = starting_letters_file.read()
    for name in names_list:
        new_letter_content = letter_contents.replace("[name]", name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as send_letters_file:
            send_letters_file.write(new_letter_content)
