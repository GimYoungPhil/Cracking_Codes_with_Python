import math

def main():
    myMessage = 'Cenoonommctmme oo snnio. s s c'
    myKey = 8

    text = decrypt(myKey, myMessage)

    print(text)

def decrypt(key, message):

    length = len(message)
    columns = key
    rows = math.ceil(length / columns)
    ciphertext = [''] * columns
    blank = (columns * rows) - length

    # 0..4
    for i in range(rows):
        index = i

        # 0..8
        for j in range(columns):

            if j > (columns - blank):
                width = (rows - 1)
            else:
                width = rows

            if j > 0:
                index += width

            if index < length:
                print('i: %s, j: %s, index: %s, char: %s' % (i, j, index, message[index]))



    return '____'


if __name__ == '__main__':
    main()
