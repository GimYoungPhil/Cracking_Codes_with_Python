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
    blank = (columns * rows) - length
    ciphertext = [''] * columns

    # i=0, message[0:4]
    # i=1, message[4:8]
    # i=2, message[8:12]
    # i=3, message[12:16]
    # i=4, message[16:20]
    # i=5, message[20:24]
    # i=6, message[24:27]
    # i=7, message[27:30]
    start = 0
    end = 0
    for i in range(columns):
        start = end

        if i < columns - blank:
            end = start + rows
        else:
            end = start + (rows - 1)

        ciphertext[i] = message[start:end]

    plaintext = ''
    for j in range(rows):
        for k in range(columns):
            if length > len(plaintext):
                plaintext += ciphertext[k][j]

    return plaintext

if __name__ == '__main__':
    main()
