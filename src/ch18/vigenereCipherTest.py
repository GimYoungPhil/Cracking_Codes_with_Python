# The Vigènre Cipher
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

    for cipher in message:
        if cipher.upper() in LETTERS:
            cipherIndex = LETTERS.find(cipher.upper())
            if mode == 'encrypt':
                cipherIndex += keyList[keyIndex]
            elif mode == 'decrypt':
                cipherIndex -= keyList[keyIndex]
            cipherIndex %= length

            plain = LETTERS[cipherIndex]
            if cipher.islower():
                plain = plain.lower()
            translated.append(plain)

            keyIndex += 1
            keyIndex %= lengthKey
        else:
            translated.append(cipher)

    return ''.join(translated)


#

if __name__ == '__main__':
    main()
