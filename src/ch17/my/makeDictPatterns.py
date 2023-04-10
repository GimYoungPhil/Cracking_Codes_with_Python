import pprint

def main():
    wordList = loadDictionary()
    patterns = makePatterns(wordList)
    patternsFormatted = pprint.pformat(patterns)
    makeDict(patternsFormatted)

    print('main...')


# () -> (['ABBA', 'ABBY', ...])
def loadDictionary():
    openFile = open('dictionary.txt')
    wordList = openFile.read().split('\n')
    openFile.close()

    return wordList


def patternDict(word):
    word = word.upper()
    dic = {}
    list = []
    counter = 0

    for ch in word:
        if ch not in dic:
            dic[ch] = str(counter)
            counter = counter + 1
        list.append(dic[ch])

    return '.'.join(list)


def makePatterns(wordList):
    patterns = {}
    
    for word in wordList:
        pattern = patternDict(word)
        if pattern in patterns:
            patterns[pattern].append(word)
        else:
            patterns[pattern] = [word]

    return patterns


# allPatterns = {
#     '0.1.0': 'MOM',
#     '0.1.0.2': 'MOMY',
# }
def makeDict(patterns, fileName = 'dictPatterns.py'):
    contents = 'allPatterns = ' + str(patterns)

    dickFile = open(fileName, 'w')
    dickFile.write(contents)
    dickFile.close()

if __name__ == '__main__':
    main()
