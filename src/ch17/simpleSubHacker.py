# Hacking The Simple Substitution Cipher
#

import os, re, copy, pyperclip, simpleSubCipher, wordPatterns, makeWordPatterns





LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLetterOrSpacePattern = re.compile('[^A-Z\s]')

def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

    #
    print('Hacking...')
    letterMapping = hackSimpleSub(message)

    #
    print('Mapping...')
    print(letterMapping)
    print()
    print('Original cphertext:')
    print(message)
    print()
    print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)


def getBlankCipherletterMapping():
    #
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def addLettersToMapping(letterMapping, cipherword, candidate):
    # letterMappint = { 'A': [], 'B': [], 'C': [], ... }
    # cipherword = 'HGHHU'
    # candidate = 'PUPPY'
    # cipherword[i] = 'H', 'G', 'H', 'H', 'U'
    # candidate[i] = 'P', 'U', 'P', 'P', 'Y'

    # 'H': ['P']
    # 'G': ['U']
    # 'U': ['Y']


    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])



def intersectMappings(mapA, mapB):
    # mapA = { A: [], B: [], C: [], ... }
    # mapB = { G: ['U', 'O', 'A'], H: ['P', 'M', 'B', 'L', 'N'],  U: ['Y', 'S']}
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:

        #
        #
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            #
            #
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
    #
    #
    #
    #
    #
    #
    #
    #

    loopAgain = True
    while loopAgain:
        #
        loopAgain = False
        #
        #

        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        #
        #
        #
        for cipherletter in LETTERS:
            print('cipherletter: ' + cipherletter)
            for s in solvedLetters:
                print('solvedLetters: ' + s)
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        #
                        loopAgain = True
    return letterMapping


def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLetterOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        #
        candidateMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue

        # candidate = 'PUPPY', 'MOMMY', 'BOBBY', ' LULLS', 'NANNY'
        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)

        #
        intersectedMap = intersectMappings(intersectedMap, candidateMap)

    #
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
    #
    #

    #
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            #
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    #
    return simpleSubCipher.decryptMessage(key, ciphertext)


if __name__ == '__main__':
    main()
