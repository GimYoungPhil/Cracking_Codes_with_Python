# The Vigenère Cipher
#

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    #
    myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    myKey = 'ASIMOV'
    myMode = 'encrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = encryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has bone copied to the clipboard.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = []

    keyIndex = 0
    key = key.upper()

    keyList = []
    lengthKey = len(key)
    length = len(LETTERS)

    for k in key:
        keyList.append(LETTERS.find(k))

    for symbol in message:
        if symbol.upper() in LETTERS:
            symbolIndex = LETTERS.find(symbol.upper())
            if mode == 'encrypt':
                symbolIndex += keyList[keyIndex]
            elif mode == 'decrypt':
                symbolIndex -= keyList[keyIndex]
            symbolIndex %= length

            letter = LETTERS[symbolIndex]
            if symbol.islower():
                letter = letter.lower()
            translated.append(letter)

            keyIndex += 1
            keyIndex %= lengthKey
        else:
            translated.append(symbol)

    return ''.join(translated)


#

if __name__ == '__main__':
    main()
