#
#

import itertools, re
import detectEnglish, vigenereCipher, pyperclip, freqAnalysis

def main():
    print()


def findRepeatSequencesSpacings(message):
    print()


def getUsefulFactors(num):
    print()


def getItemAtIndexOne(x):
    return x[1]


def getMostCommonFactors(seqFactors):
    print()


def kasiskiExamination(ciphertext):
    print()


def getNthSubkeysLetters(nth, keyLength, message):
    print()


def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
    print()


def hackVigenere(ciphertext):
    # ['AICK', 'AICN', 'AICR', 'AICV', 'AICY', ...]
    for key in keyList:
        decryptedText = vigenereCipher.decryptMessage(key, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPersentage=40):
            #
            print()
            print('Possible encryption break:')
            print('Key ' + str(key) + ': ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main()__':
    main()
