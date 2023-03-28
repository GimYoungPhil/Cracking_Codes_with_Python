# qeFIP?eGSeECNNS,
# 5coOMXXcoPSZIWoQI,
# avnl1olyD4l\'ylDohww6DhzDjhuDil,
# z.GM?.cEQc. 70c.7KcKMKHA9AGFK,
# ?MFYp2pPJJUpZSIJWpRdpMFY,
# ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K
# Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA

# Key #34: I love my kitty,
# Key #44: My kitty loves me,
# Key #7: Together we're happy as can be,
# Key #32: Though my head has suspicions,
# Key #45: That I keep under my hat,
# Key #11: Of what if I shrank to the size of a rat.
# Key #1: Yeah, she would probably eat me.

message = 'Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#
for key in range(len(SYMBOLS)):
    #
    #
    translated = ''

    #

    #
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            #
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            #
            translated = translated + SYMBOLS[translatedIndex]

        else:
            #
            translated = translated + symbol

    #
    print('Key #%s: %s' % (key, translated))
