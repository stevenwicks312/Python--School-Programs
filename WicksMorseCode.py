morseCode = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
             'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
              'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def receive(receiveCode): ##Convert morse code into written english
    receiveCode += ' '
    code = ''
    text = ''
    for letters in receiveCode:
        if letters != ' ':
            i = 0 ##Doesn't count spaces as letters
            text += letters
        else:
            i += 1
            if i ==2:
                code += ' ' ## add spaces to separate letters
            else:   ##Converts the values(morse) into the keys(letters)
                code += list(morseCode.keys())[list(morseCode.values()).index(text)]
                text = ''
    return code

def send(sendCode): ##Written statements into morse code
    code = ''
    for letters in sendCode:
        if letters != ' ': ## single spaces to separate letters
            code +=morseCode[letters]+' '
        else:
            code +=' ' ##double space to seperate words
    return code

def MorseToEnglish(receiveCode):  #,receiveCode
    try:
        if receiveCode != None:
            message = receive(receiveCode.upper())
            print("Decrypted Code: "+ message)
            return message
    except ValueError:
        print("***Error: Invalid characters used when "
              "converting Morse Code to English\n")

def EnglishToMorse(sendCode):
    try:
        if sendCode != None:
            message = send(sendCode.upper()) #Turns lowercase text to uppercase
            print("Encrypted Code: " + message)
            return message
    except KeyError:
        print("***Error: Invalid characters used when converting English to Morse Code\n")



