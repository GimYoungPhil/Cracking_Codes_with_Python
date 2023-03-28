message = 'Common sence is not so common.'

key = 8

translated = ''

# i = 0, 1, 2, 3, 4, 5, 6, 7
# j = 0, 8, 16, 24
for i in range(key):
    # print('i: %s' % (i))

    for j in [0, 8, 16, 24]:
        # print('j: %s' % (j))

        index = i + j

        if index < len(message):
            letter = message[index]
            translated = translated + letter

print(translated)

