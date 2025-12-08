#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
names = []
with open("Input/Names/invited_names.txt") as file:
    names = file.read().split("\n")
for name in names:
    newText = ""
    newFile = open(f"Output/{name}'s Invitation.txt", mode="x")
    with open("Input/Letters/ReadyToSend/starting_letter.txt") as file:
        contents = file.read()
        fileList = contents.split("[name]")
        newText = name.join(fileList)
    newFile.write(newText)
    newFile.close()