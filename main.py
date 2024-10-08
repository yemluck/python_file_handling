PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    #print(names_list)

with open("Input/Letters/starting_letter.txt") as draft:
    letter = draft.read()
    #print(letter)
    for name in names_list:
        stripped_name = name.strip()
        final_draft = letter.replace(PLACEHOLDER, stripped_name)
        final_draft = final_draft.replace("Angela", "Chris")
        with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as ol:
            ol.write(final_draft)



