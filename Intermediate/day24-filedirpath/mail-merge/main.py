with open("./mail-merge/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

names = []
placeholder = "[name]"

with open("./mail-merge/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    
for name in names:
    name = name.strip()
    new_letter = letter.replace(placeholder,name)
    
    with open(f"./mail-merge/Output/ReadyToSend/{name}.txt", "w") as file:
        file.write(new_letter)
