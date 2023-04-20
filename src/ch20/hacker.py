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



def messageDecrypt(message):
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



# 0: AICK [0, 0, 0, 0]    10: IICK [1, 0, 0, 0]    20: NICK [2, 0, 0, 0]
# 1: AICN [0, 0, 0, 1]    11: IICN [1, 0, 0, 1]    21: NICN [2, 0, 0, 1]
# 2: AICR [0, 0, 0, 2]    12: IICR [1, 0, 0, 2]    22: NICR [2, 0, 0, 2]
# 3: AICV [0, 0, 0, 3]    13: IICV [1, 0, 0, 3]    23: NICV [2, 0, 0, 3]
# 4: AICY [0, 0, 0, 4]    14: IICY [1, 0, 0, 4]    24: NICY [2, 0, 0, 4]
# 5: AZCK [0, 1, 0, 0]    15: IZCK [1, 1, 0, 0]    25: NZCK [2, 1, 0, 0]
# 6: AZCN [0, 1, 0, 1]    16: IZCN [1, 1, 0, 1]    26: NZCN [2, 1, 0, 1]
# 7: AZCR [0, 1, 0, 2]    17: IZCR [1, 1, 0, 2]    27: NZCR [2, 1, 0, 2]
# 8: AZCV [0, 1, 0, 3]    18: IZCV [1, 1, 0, 3]    28: NZCV [2, 1, 0, 3]
# 9: AZCY [0, 1, 0, 4]    19: IZCY [1, 1, 0, 4]    29: NZCY [2, 1, 0, 4]
#         i / (50 / 5)      [2 * 1 * 5]
#        (i % 10) / 5 []

# [
#     ['A', 'I', 'N', 'W', 'X'],
#     ['I', 'Z'],
#     ['C'],
#     ['K', 'N', 'R', 'V', 'Y'],
# ]
def getKeyList(keyList):
    keyword = []

    totalLength = 1
    keyLengthList = []
    for keys in keyList:
        lengthKeys = len(keys)
        keyLengthList.append(lengthKeys)
        totalLength *= lengthKeys

    print(keyLengthList)
    reversedList = keyLengthList.copy()
    reversedList.reverse()

    print(reversedList)

    for i in range(totalLength):
        word = []

        for keys in keyList:
            word.append(keys[i % len(keys)])
        # 0
        # word.append(keyList[0][i % lengthList[0]])
        # word.append(keyList[1][i % lengthList[1]])
        # word.append(keyList[2][i % lengthList[2]])
        # word.append(keyList[3][i % lengthList[3]])

        keyword.append(''.join(word))
        keyword.sort()

    return keyword


# ('string', 3)
def getKeyListWithKeyLength(message, keyLength):

    # { 0: 'string', 1: 'string', 2: 'string' }
    messageCut = cutMessage(message, keyLength)

    # [['A', 'I', 'N', 'W', 'X'], 1: ['I', 'Z'], 2: ['C'], 3: ['K', 'N', 'R', 'V', 'Y']]
    keyList = []

    for index in range(keyLength):
        keyList.append(messageDecrypt(messageCut[index]))

    print(keyList)

    keys = getKeyList(keyList)
    print(keys)


    # print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, ))

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
