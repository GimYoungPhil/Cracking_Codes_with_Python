# Hacking The Vigenère Cipher
#

import vigenereCipher, freqAnalysis

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def simpleText(message):
    text = []

    for symbol in message:
        if symbol.upper() in LETTERS:
            text.append(symbol.upper())
    return ''.join(text)



def findDistance(message, lengthWord = 3):
    # [('YBN', 8), ('AZU', 48), ('VRA', 8), ('VRA', 32), ('VRA', 24)]
    record = []
    lengthMessage = len(message)
    wordRange = lengthMessage + 1 - (lengthWord * 2)
    candRange = lengthMessage + 1 - (lengthWord * 1)

    for wordIndex in range(wordRange):

        word = message[wordIndex:wordIndex + lengthWord]

        for candIndex in range(wordIndex + lengthWord, candRange):

            cand = message[candIndex:candIndex + lengthWord]

            if word == cand:
                record.append((word, candIndex - wordIndex))

    return record



# [('YBN', 8), ('AZU', 48), ('VRA', 8), ('VRA', 32), ('VRA', 24)]
def orderDistance(tupleList):

    # [ 8, 48, 32, 24]
    distanceList = []
    for (word, distance) in tupleList:
        if distance not in distanceList:
            distanceList.append(distance)
        

    # [8, 24, 32, 48]
    distanceList.sort()

    return distanceList



# 48
def getFactors(num):
    factors = []

    for f in range(2, num + 1):
        if num % f == 0:
            factors.append(f)

    # [2, 3, 4, 6, 8, 12, 16, 24, 48]
    return factors



# [8, 24, 32, 48]
def getDoubleFactors(numbers):
    doubleList = []

    for number in numbers:
        factorList = getFactors(number)
        doubleList.append(factorList)

    # [
    #     [2, 4, 8]
    #     [2, 3, 4, 6, 8, 12, 24]
    #     [2, 4, 8, 16, 32]
    #     [2, 3, 4, 6, 8, 12, 16, 24, 48]
    # ]
    return doubleList



# [
#     [2, 4, 8]
#     [2, 3, 4, 6, 8, 12, 24]
#     [2, 4, 8, 16, 32]
#     [2, 3, 4, 6, 8, 12, 16, 24, 48]
# ]
def getFactorCount(doubleList):
    # {2: 4, 3: 2, 4: 4, 6: 2, 8: 4, 12: 2, 24: 2, 16: 2, 48: 1, 32: 1}
    counter = {}

    for oneList in doubleList:
        for factor in oneList:
            if factor not in counter:
                counter[factor] = 1
            else:
                counter[factor] += 1

    return counter


def getItemAtIndexZero(items):
    return items[0]


def getCounterOrder(doubleList):
    factorToCount = getFactorCount(doubleList)

    # { 2: [3, 6, 12, 24, 16], 4: [2, 4, 8], 1: [28, 32] }
    countToFactor = {}
    for factor in factorToCount:
        if factorToCount[factor] not in countToFactor:
            countToFactor[factorToCount[factor]] = [factor]
        else:
            countToFactor[factorToCount[factor]].append(factor)

    # { 2: [24, 16, 12, 6, 3], 4: [8, 4, 2], 1: [32, 28] }
    for count in countToFactor:
        countToFactor[count].sort(reverse=False)

    # [(2, [24, 16, 12, 6, 3]), (4, [8, 4, 2]), (1, [32, 28])]
    countPairs = list(countToFactor.items())

    # [(4, [8, 4, 2]), (2, [24, 16, 12, 6, 3]), (1, [32, 28])]
    countPairs.sort(key=getItemAtIndexZero, reverse=True)

    # [8, 4, 2, 24, 16, 12, 6, 3, 32, 28]
    countOrder = []
    for countPair in countPairs:
        countOrder.extend(countPair[1])

    return countOrder



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



def messageDecrypt(message, limitScore = 2):
    keyList = []

    for subkey in LETTERS:
        decryptMessage = vigenereCipher.decryptMessage(subkey, message)
        score = freqAnalysis.englishFreqMatchScore(decryptMessage)
        if score >= limitScore:
            keyList.append(subkey)

    # ['A', 'G', 'H', 'I', 'M', 'N', 'P', 'T', 'V']
    return keyList



# ('string', 3)
def getKeyListWithKeyLength(message, keyLength):

    # { 0: 'string', 1: 'string', 2: 'string' }
    messageDick = cutMessage(message, keyLength)
    for index in range(keyLength):
        messageDick[index] = messageDecrypt(messageDick[index])


    


    print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, ))

    # [1번째 후보 문자], [2번째 후보 문자], [3번째 후보 문자]
    # [['A', 'L', 'M'], ['S', 'N', 'O'], ['V', 'I', 'Z']]
    return []



def main():
    ciphertext = """
PPQCA XQVEKG YBNKMAZU YBNGBAL JON I TSZM JYIM.
VRAG VOHT VRAU C TKSG. DDWUO XITLAZU VAVV RAZ C VKB QP IWPOU.
"""
    # hackedMessage = simpleText(ciphertext)
    # findDistance(hackedMessage)


    # if hackedMessage != None:
    #     print('Copying hacked message to clipboard:')
    #     print(hackedMessage)
    # else:
    #     print('Failed to hack encryption.')

if __name__ == '__main__':
    main()
