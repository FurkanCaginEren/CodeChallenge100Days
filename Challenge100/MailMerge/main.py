# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("MailMerge/Input/Names/invited_names.txt") as file:
    data = file.readlines()


with open("MailMerge/Input/Letters/starting_letter.txt", mode="r+") as file:
    text = file.read()


for name in data:
    new_data = name.strip()
    new_text = text.replace("[name]", new_data)
    with open(f"MailMerge/Output/ReadyToSend/letter_for_{new_data}.txt", mode="w") as file:
        file.write(new_text)
