# Transposition Encrypt
#

import pyperclip

def main():
    # myMessage = 'Common sence is not so common.'
    myMessage = 'Then they trotted away for the wind grew high: One acorn they left, and no more might you spy.'
    myKey = 9

    ciphertext = encryptMessage(myKey, myMessage)

    #
    #
    #
    print(ciphertext + '|')

    #
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    #
    ciphertext = [''] * key

    # 0..8
    for column in range(key):
        currentIndex = column

        #
        while currentIndex < len(message):
            #
            #
            ciphertext[column] += message[currentIndex]

            #
            currentIndex += key

    #
    return ''.join(ciphertext)


#

if __name__ == '__main__':
    main()
