'''
The caesar function will be used to encrypt or decrypt user input.

@parameters:
    text = string provided as encrypt or decrypt text.
    shift = number that is use to perform an alphabetically position shift in the list.
    operation = string letter "e" for encrypt and "d" for decrypt.

@return:
    if operation is "e" then the function will return the encrypted text.
    if operation is "d" then the function will return the decrypted text.
'''

def caesar(text, shift, operation):    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Your code goes here
    encrypt_message = ""
    if operation == "e":
        try:
            for letter in text:
                if letter in alphabet:
                    if 0 <= int(shift) <= 25:
                        #shift_index will shift alphabet seed by user's input shift value
                        shift_index = (alphabet.index(letter) + int(shift)) % 26
                        #encrypt_message will add alphabet at shift_index value to the empty encrypt_message
                        encrypt_message += alphabet[shift_index]
                    else:
                        return "invalid shift"
            return encrypt_message
        except ValueError:
            return "invalid shift"

    decrypt_message = ""
    if operation == "d":
        try:
            for letter in text:
                if letter in alphabet:
                        if 0 <= int(shift) <= 25:
                            #shift_index_0 will shift alphabet seed by user's input shift value
                            shift_index_0 = (alphabet.index(letter) - int(shift)) % 26
                            #decrypt_message will add alphabet at shift_index_0 value to the empty decrypt_message
                            decrypt_message += alphabet[shift_index_0]
                        else:
                            return "invalid shift"
            return decrypt_message
        except ValueError:
            return "invalid shift"
    else:
        return "invalid option"

    
    

              
