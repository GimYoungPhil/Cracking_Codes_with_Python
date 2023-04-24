# Hacking The Vigenère Cipher
#

import re
import vigenereCipher, freqAnalysis, pyperclip, detectEnglish

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX_KEY_LENGTH = 16
NUM_MOST_FREQ_LETTERS = 4
SILENT_MODE = False
NONLETTERS_PATTERN = re.compile('[^A-Z]')


def main():
    ciphertext = """PPQCA XQVEKG YBNKMAZU YBNGBAL JON I TSZM JYIM. VRAG VOHT VRAU C TKSG. DDWUO XITLAZU VAVV RAZ C VKB QP IWPOU."""
    hackedMessage = hackVigenera(ciphertext)

    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def findRepeatSequencesSpacings(message):

    message = NONLETTERS_PATTERN.sub('', message.upper())

    seqSpacings = {}

    for seqLength in range(3, 6):

        messageLimit = len(message) - seqLength

        for seqStart in range(messageLimit):

            seq = message[seqStart:seqStart + seqLength]

            for candStart in range(seqStart + seqLength, messageLimit):

                cand = message[candStart:candStart + seqLength]

                if seq == cand:
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []

                    seqSpacings[seq].append(candStart - seqStart)

    # { 'VRA': [8, 24, 32], 'AZU': [48], 'YBN': [8] }
    return seqSpacings



def getUsefulFactors(num):

    if num < 2:
        return []

    factors = []

    for f in range(2, MAX_KEY_LENGTH + 1):
        if num % f == 0:
            factors.append(f)

    # [2, 3, 4, 6, 8, 12, 16, 24, 48]
    return factors



def getItemAtIndexOne(items):
    return items[1]



def getMostCommonFactors(seqFactors):

    factorCounts = {}

    for seq in seqFactors:
        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] = 0
            factorCounts[factor] += 1

    factorsByCount = []
    for factor in factorCounts:
        factorsByCount.append((factor, factorCounts[factor]))

    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

    return factorsByCount



def cutMessage(message, length):
    # { 0: [], 1: [], 2: [] }
    messageLength = len(message)
    messageDick = {}
    for i in range(length):
        messageDick[i] = []

    for index in range(messageLength):
        messageDick[index % length].append(message[index])

    # { 0: [], 1: [], 2: [] }
    for i in range(length):
        messageDick[i] = ''.join(messageDick[i])

    # { 0: 'string', 1: 'string', 2: 'string' }
    return messageDick



def messageDecrypt1(message):
    # { 2: ['A', 'I', 'N'], 1: ['B', 'C'] }
    scoreDick = {}
    maxScore = 0

    for subkey in LETTERS:
        decryptMessage = vigenereCipher.decryptMessage(subkey, message)
        score = freqAnalysis.englishFreqMatchScore(decryptMessage)

        if score > maxScore:
            maxScore = score

        if score not in scoreDick:
            scoreDick[score] = [subkey]
        else:
            scoreDick[score].append(subkey)

    # ['A', 'G', 'H', 'I', 'M', 'N', 'P', 'T', 'V']
    return scoreDick[maxScore]



def messageDecrypt(message):
    # [('A', 2), ('B', 1), ('C', 0), ... ]
    scoreList = []

    for subkey in LETTERS:
        decryptMessage = vigenereCipher.decryptMessage(subkey, message)
        score = freqAnalysis.englishFreqMatchScore(decryptMessage)

        scoreList.append((subkey, score))

    scoreList.sort(key=getItemAtIndexOne, reverse=True)

    topScore = []

    # [('A', 2), ('I', 2), ('N', 2), ('W', 2)]
    for letterAndScore in scoreList[:NUM_MOST_FREQ_LETTERS]:
        topScore.append(letterAndScore[0])

    #['A', 'I', 'N', 'W']
    return topScore



def makeMatrix(listA, listB):
    matrix = []
    for elementsA in listA:
        for elementsB in listB:
            temp = []
            temp.extend(elementsA)
            temp.extend(elementsB)
            matrix.append(temp)

    return matrix



def makeMatrix2(listA, listB):
    lenA = len(listA)
    lenB = len(listB)
    matrix = []

    for index in range(lenA * lenB):
        temp = []
        temp.extend(listA[int(index / lenB)])
        temp.extend(listB[int(index % lenB)])
        matrix.append(temp)

    return matrix



def makeMatrix3(dobuleList):
    matrix = []
    firstList = dobuleList[0]
    restList = dobuleList[1:]
    for firstElement in firstList:
        for nextList in restList:
            nextEmpt = []
            for element in nextList:
                empt = []
                empt.append(firstElement)
                empt.append(element)
            nextEmpt.append(empt)

    return matrix



def makeMatrix4(dobuleList):

    matrix = []

    for innerList in dobuleList:
        if len(matrix) == 0:
            matrix.extend(innerList)
        else:
            tempList = []
            for elementMatrix in matrix:
                for elemtntInner in innerList:
                    innerTemp = []
                    innerTemp.extend(elementMatrix)
                    innerTemp.extend(elemtntInner)
                    tempList.append(innerTemp)
            matrix = tempList
    # [
    #     ['A', 'I', 'C', 'K'],
    #     ['A', 'I', 'C', 'N'],
    #     ['A', 'I', 'C', 'R'],
    #     ['A', 'I', 'C', 'V'],
    #     ['A', 'I', 'C', 'Y'],
    #     ...
    # ]
    return matrix



# [
#     ['A', 'I', 'C', 'K'],
#     ['A', 'I', 'C', 'N'],
#     ['A', 'I', 'C', 'R'],
#     ['A', 'I', 'C', 'V'],
#     ['A', 'I', 'C', 'Y'],
#     ...
# ]
def getKeywordList(dobuleList):
    empty = []
    for innerList in dobuleList:
        keyword = ''.join(innerList)
        empty.append(keyword)

    return empty



# ('string', 3)
def getKeyListWithKeyLength(ciphertext, keyLength):

    ciphertextUp = ciphertext.upper()

    message = NONLETTERS_PATTERN.sub('', ciphertextUp)

    # { 0: 'string', 1: 'string', 2: 'string' }
    messageCut = cutMessage(message, keyLength)

    # [
    #     [('A', 2), ('I', 2), ('N', 2), ('W', 2)],
    #     [('I', 3), ('Z', 3), ('A', 2), ('E', 2)],
    #     [('C', 3), ('G', 2), ('H', 2), ('I', 2)],
    #     [('K', 2), ('N', 2), ('R', 2), ('V', 2)]
    # ]
    allFreqScores = []

    for index in range(keyLength):
        allFreqScores.append(messageDecrypt(messageCut[index]))

    if not SILENT_MODE:
        for i in range(len(allFreqScores)):
            print('Possible letters for letter %s of the key: ' % (i + 1), end='')
            for letter in allFreqScores[i]:
                print('%s ' % letter, end='')
            print()

    keywordMatrix = makeMatrix4(allFreqScores)
    keywordList = getKeywordList(keywordMatrix)

    for keyword in keywordList:
        if not SILENT_MODE:
            print('Attempting with key: %s' % (keyword))

        decryptedText = vigenereCipher.decryptMessage(keyword, ciphertextUp)

        if detectEnglish.isEnglish(decryptedText):
            origCase = []
            for i in range(len(ciphertext)):
                if ciphertext[i].isupper():
                    origCase.append(decryptedText[i].upper())
                else:
                    origCase.append(decryptedText[i].lower())
            decryptedText = ''.join(origCase)

            print('Possible encryption hack with key %s:' % (keyword))
            print(decryptedText[:200]) # Only show first 200 characters.
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None



def kasiskiExamination(ciphertext):

    # 1. 반복되는 문자열(3~5)간의 간견 찾기
    repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)

    # 2. 간격들의 약수들을 계산하기
    seqFactors = {}
    for seq in repeatedSeqSpacings:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacings[seq]:
            seqFactors[seq].extend(getUsefulFactors(spacing))

    # 3. 가장 많이 반복되는 약수 순서로 정리하기
    # [(2, 5), (4, 5), (8, 5), (3, 2), (6, 2), (12, 2), (16, 2)]
    factorsByCount = getMostCommonFactors(seqFactors)
    allLikelyKeyLengths = []
    for lengthAndFreq in factorsByCount:
        allLikelyKeyLengths.append(lengthAndFreq[0])

    # [2, 4, 8, 3, 6, 12, 16]
    return allLikelyKeyLengths


def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
    # ciphertextUp = ciphertext.upper()
    message = NONLETTERS_PATTERN.sub('', ciphertext.upper())

    allFreqScores = []

    cutDict = cutMessage(message, mostLikelyKeyLength)
    for index in cutDict:
        freqScores = []
        for possibleKey in LETTERS:
            decryptedText = vigenereCipher.decryptMessage(possibleKey, cutDict[index])
            keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
            freqScores.append(keyAndFreqMatchTuple)

        freqScores.sort(key=getItemAtIndexOne, reverse=True)
        print(freqScores)
        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

    # [[('C', 5), ('I', 4), ('B', 3), ('G', 3)], [('K', 6), ('R', 6), ('V', 6), ('G', 4)]]
    print(allFreqScores)

    if not SILENT_MODE:
        for i in range(len(allFreqScores)):
            print('Possible letters for letter %s of the key: ' % (i + 1), end='')
            for freqScore in allFreqScores[i]:
                print('%s ' % freqScore[0], end='')
            print()



def hackVigenera(ciphertext):
    allLikelyKeyLengths = [4, 3, 2]
    # allLikelyKeyLengths = kasiskiExamination(ciphertext)
    if not SILENT_MODE:
        keyLengthStr = ''
        for keyLength in allLikelyKeyLengths:
            keyLengthStr += '%s ' % (keyLength)
        print('Kasiski examination results say the most likely key lengths are: ' + keyLengthStr + '\n')

    hackedMessage = None
    for keyLength in allLikelyKeyLengths:
        if not SILENT_MODE:
            print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
        hackedMessage = getKeyListWithKeyLength(ciphertext, keyLength)
        if hackedMessage != None:
            break

    # hackedMessage = None
    # for keyLength in allLikelyKeyLengths:
    #     if not SILENT_MODE:
    #         print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
    #     hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
    #     if hackedMessage != None:
    #         break

    #
    # if hackedMessage == None:
    #     if not SILENT_MODE:
    #         print('Unable to hack message with likely key length(s). Brute-forcing key length...')

    return hackedMessage

if __name__ == '__main__':
    main()
