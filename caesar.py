# Indumathi Prakash

def caesar_encrypt(key, message):
    """Encrypt a message"""
    #changing all characters to be uppercase
    message_up = message.upper()
    #defining a new string
    encrypt = ""
    #65-90
    #looping through the message to get each character
    for char in message_up:
        # defining new_char variable as the ascii number + the key for the shift
        new_char = ord(char) + key
        if char == " " or char == ".":
            new_char = char
            encrypt += new_char
        # If the shift goes beyond 90, then it loops around
        elif new_char > 90:
            difference = new_char - 90
            next_char = 64 + difference
            # After the loop around, the number is converted back to character and added to new string encrypt
            encrypt += chr(next_char)
        # If no loop around was needed then the shifted character is added directly to encrypt
        else:
            encrypt += chr(new_char)
    return encrypt


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
    

print(caesar_encrypt(12, "Experience is the teacher of all things."))
print(caesar_decrypt(12, "QJBQDUQZOQ UE FTQ FQMOTQD AR MXX FTUZSE."))
    
            




        