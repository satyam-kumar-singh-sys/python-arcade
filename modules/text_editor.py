def use_text_editor(): 
    import os

    filename = input("Enter the filename to open or create: ")
    text =[]

    #creating a new file in case the file doesn't exist
    if not os.path.exists(filename):
        print(f"{filename} not found. Creating a new file.")
        with open(filename, "w") as file:
            pass
    else:
        with open(filename, "r") as file:
            pass

    #The text editor main code
    print("Enter your text (type 'SAVE on a new line to save and exit):")
    while True:
        editortext = input()
        if editortext.strip() == "SAVE":
            break
        text.append(editortext)

    while True:
        overwrite_or_append = input("Do you want to (o)verwrite or (a)ppend the file?: ")
        if overwrite_or_append == "o" or "a":
            break
        else:
            print("Choose between (o/a).")

    #if user chooses to append the file
    if overwrite_or_append == "a":
        with open(filename, "a") as file:
            for line in text:
                file.write(f"{line} \n")

    #if user chooses to overwrite the file
    elif overwrite_or_append == "o":
        with open(filename, "w") as file:
            for line in text:
                file.write(f"{line} \n")   

    print(f"File {filename} saved.")
    return