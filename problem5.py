#Indumathi Prakash
"""The key is 11 and the message is BELIEVE YOU CAN AND YOU ARE HALFWAY THERE. 
    My approach was to split the encrypted message into seperate words and then for each key 
    loop through and check if the word is found in common words. If the words existed in common words then I would 
    print the word and key."""





def caesar_decrypt(key, message):
    """Decrypt a message"""
    #changing all characters to be uppercase
    message_up = message.upper()
    #defining a new string
    decrypt = ""
    #65-90
    #looping through the message to get each character
    for char in message_up:
        # defining new_char variable as the ascii number + the key for the shift
        new_char = ord(char) - key
        if char == " " or char == ".":
            new_char = char
            decrypt += new_char
        # If the shift goes below 65, then it loops around
        elif new_char < 65:
            difference = 65 - new_char
            next_char = 91 - difference
            # After the loop around, the number is converted back to character and added to new string encrypt
            decrypt += chr(next_char)
        # If no loop around was needed then the shifted character is added directly to encrypt
        else:
            decrypt += chr(new_char)
    return decrypt


print()

def process_file(filename): 
    """Read, sort and return a file"""

    # checking if there are any errors opening the file and reading it 
    try:
        f = open(filename, 'r')
        text_file = f.readlines()

    # If there is an error
    except:
        print("There was an error opening the file")
        return (filename, [], 0)
    
    # If there is no error
    else:
        #Setting the number of lines to 0
        number_of_lines = 0
        # defining a new list
        strp_lst = []
        #Going line by line in the text file
        for line in text_file:
            # Getting rid of the whitespaces in each line
            stripped = line.strip()
            # adding each stripped line to the new list
            strp_lst.append(stripped)
            #counting the number of lines
            number_of_lines += 1

        #sorting the list
        sorted_items = sorted(strp_lst)

        # Return a tuple
        return (filename, sorted_items, number_of_lines) 


# Snippet to run function
(filename, items, lines) = process_file("common_words.txt")





# Set a new set to to the common words so that there is no repeat
words_set = set(items) 

# Loop thorugh decrypting for all the keys
for key in range(0, 26):
    # The message is the decrypted version
    new_message = caesar_decrypt(key, "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp")
    #Split the decrypted string into its seperate word parts
    newest_message = new_message.split(" ")
    #Loop through and check if each word in the decrypted is a common word
    for word in newest_message:
        # If it is not, then break out of the loop
        if word.lower() not in words_set:
            break
        # If it is a common word then print it out
        else:
            print(f"The key is {key}") 
            print(word)
    

# After I saw the key was 11 from above testing
print(caesar_decrypt(11, "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"))


