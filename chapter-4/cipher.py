def cipher():
    words = raw_input("enter you message to be encoded: ")
    key = int(raw_input("enter a number to be a key: "))
    splitWords = words.split()
    cipheredMessage = ""
    # print splitWords
    for word in splitWords:
        for letter in word:
            letternumber = (ord(letter) - 97 + key)%26 + 97
            #print letternumber
            letter = chr(letternumber)
            cipheredMessage += letter
        cipheredMessage += " "
    print "Ciphered Message: " + cipheredMessage
    print "Deciphered message: " + decipher(cipheredMessage, key)

def decipher(words, key):
    splitWords = words.split()
    decipheredMessage = ""
    for word in splitWords:
        for letter in word:
            letternumber = (ord(letter) - 97 - key)%26 + 97
            letter = chr(letternumber)
            decipheredMessage += letter
        decipheredMessage += " "
    return decipheredMessage

cipher()
