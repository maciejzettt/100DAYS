
with open("Input/Names/invited_names.txt", mode='r') as f:
    recipients = f.readlines()

with open("Input/Letters/starting_letter.txt", mode='r') as f:
    base_letter = f.read()

for name in recipients:
    name = name.strip()
    filename = "letter_for_" + name + '.txt'
    customized_letter = base_letter.replace('[name]', name)
    with open("Output/ReadyToSend/"+filename, mode='w') as f:
        f.write(customized_letter)
