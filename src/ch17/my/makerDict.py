def main():
    pattern = makeDick('Puppy')
    print('Puppy: ' + pattern)

    pattern = makeDick('mommy')
    print('mommy: ' + pattern)

    pattern = makeDick('Motorcycles')
    print('Motorcycles: ' + pattern)

def makeDick(word):
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


if __name__ == '__main__':
    main()
