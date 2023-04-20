import hacker


def main():
    print('Texting')
    print()


    print('1. simpleText:')
    message = """PPQCA XQVEKG YBNKMAZU YBNGBAL JON I TSZM JYIM. VRAG VOHT VRAU C TKSG. DDWUO XITLAZU VAVV RAZ C VKB QP IWPOU."""
    hackedMessage = hacker.simpleText(message)
    print(hackedMessage)
    print()


    print('2. findDistance:')
    tupleList = hacker.findDistance(hackedMessage)
    print(tupleList)
    print()


    print('3. orderDistance:')
    distanceList = hacker.orderDistance(tupleList)
    print(distanceList)
    print()


    print('4. getDoubleFactors:')
    doubleFactors = hacker.getDoubleFactors(distanceList)
    print(doubleFactors)
    print()


    print('5. getCounterOrder:')
    distances = hacker.getCounterOrder(doubleFactors)
    print(distances)
    print()


    # print('cutMessage')
    # ddd = hacker.cutMessage(hackedMessage, 3)
    # print(ddd)


    # print('messageDecrypt')
    # keyList = hacker.messageDecrypt(ddd[0])
    # print(keyList)


    # getKeyListWithKeyLength
    print('6. getKeyListWithKeyLength')
    messageDick = hacker.getKeyListWithKeyLength(hackedMessage, distances[1])
    print(messageDick)


    # f = [
    #     [2, 3, 4, 6, 8, 12, 24],
    #     [2, 4, 8],
    #     [2, 3, 4, 6, 8, 12, 16, 24, 48],
    #     [2, 4, 8, 16, 32],
    # ]
    # result = countFactors(f)
    # print(result)

if __name__ == '__main__':
    main()
