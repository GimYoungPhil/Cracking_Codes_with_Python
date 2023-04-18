# Hacking The Vigenère Cipher
#

# import detectEnglish, vigenereCipher

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def simpleText(message):

    text = []
    for symbol in message:
        if symbol.upper() in LETTERS:
            text.append(symbol.upper())
    return ''.join(text)


def findWord(message):
    record = []
    length = len(message)
    wordLen = 3
    wordRange = length + 1 - (wordLen * 2)
    candRange = length + 1 - (wordLen * 1)

    for wordIndex in range(wordRange):

        word = message[wordIndex:wordIndex + wordLen]
        # print('%s: [%s:%s]' % (word, wordIndex, wordIndex + wordLen))
        # candis = []

        for candIndex in range(wordIndex + wordLen, candRange):

            cand = message[candIndex:candIndex + wordLen]
            # candis.append(cand)

            if word == cand:
                record.append((word, wordIndex, candIndex, cand))
        
        # print(len(candis))

    print(record)



def main():
    ciphertext = """
Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi,
lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf."""
    hackedMessage = simpleText(ciphertext)
    findWord(hackedMessage)

    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')

if __name__ == '__main__':
    main()
