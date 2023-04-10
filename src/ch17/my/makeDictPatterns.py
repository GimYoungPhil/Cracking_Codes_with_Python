import pprint

def main():
    words = loadDictionary()
    dicts = makeDict(words)
    dicts = pprint.pformat(dicts)
    writeDict(dicts)


def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords


def patternDict(word):
    word = word.upper()
    dic = {}
    list = []
    counter = 0

    for ch in word:
        if ch in dic:
            list.append(dic[ch])
        else:
            character = str(counter)
            dic[ch] = character
            list.append(character)
            counter = counter + 1

    return '.'.join(list)


def makeDict(words):
    dictionary = {}
    
    for word in words:
        pattern = patternDict(word)
        if pattern in dictionary:
            dictionary[pattern].append(word)
        else:
            dictionary[pattern] = [word]

    return dictionary


# allPatterns = {
#     '0.1.0': 'MOM',
#     '0.1.0.2': 'MOMY',
# }
def writeDict(dicts, fileName = 'dictPatterns.py'):
    contents = 'allPatterns = ' + str(dicts)

    dickFile = open(fileName, 'w')
    dickFile.write(contents)
    dickFile.close()

if __name__ == '__main__':
    main()
