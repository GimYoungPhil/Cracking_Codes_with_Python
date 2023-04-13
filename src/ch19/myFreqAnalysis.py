# Frequency Analysis
#


ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
    # String
    # { A: [1], B: [2], C: [3], ... }
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount


# String
# 'EASHOTIRNDGCLUYVFMBWJKXPQZ'
def getFrequencyOrder(message):

    dictionary = getLetterCount(message)

    # [('E', 30), ('A', 27), ('S', 23), ...]
    sorted_dictionary = sorted(dictionary.items(), key = lambda item: item[1], reverse = True)

    SYMBOLS = []
    for (symbol, count) in sorted_dictionary:
        SYMBOLS.append(symbol)

    return ''.join(SYMBOLS)



def englishFreqMatchScore(message):
    # 
    # ETAOIN | SHRDLCUMWFGYPB | VKJXQZ
    # ‾‾‾‾‾‾                    ‾‾‾‾‾‾
    # EISNTH | AOCLRFDGWVMUYB | PZXQJK
    # ‾‾ ‾‾                      ‾‾‾‾‾
    #

    freqOrder = getFrequencyOrder(message)

    print('freqOrder: ', freqOrder)

    matchScore = 0

    for commonLetter in ETAOIN[0:6]:
        if commonLetter in freqOrder[0:6]:
            matchScore += 1

    for rareLetter in ETAOIN[-6:]:
        if rareLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore


def main():
    myMessage = """
Alan Mathison Turing OBE FRS (/ˈtjʊərɪŋ/; 23 June 1912 – 7 June 1954) was an English mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist.[6] Turing was highly influential in the development of theoretical computer science, providing a formalisation of the concepts of algorithm and computation with the Turing machine, which can be considered a model of a general-purpose computer.[7][8][9] He is widely considered to be the father of theoretical computer science and artificial intelligence.[10]
Born in Maida Vale, London, Turing was raised in southern England. He graduated at King's College, Cambridge, with a degree in mathematics. Whilst he was a fellow at Cambridge, he published a proof demonstrating that some purely mathematical yes–no questions can never be answered by computation and defined a Turing machine, and went on to prove that the halting problem for Turing machines is undecidable. In 1938, he obtained his PhD from the Department of Mathematics at Princeton University. During the Second World War, Turing worked for the Government Code and Cypher School at Bletchley Park, Britain's codebreaking centre that produced Ultra intelligence. For a time he led Hut 8, the section that was responsible for German naval cryptanalysis. Here, he devised a number of techniques for speeding the breaking of German ciphers, including improvements to the pre-war Polish bomba method, an electromechanical machine that could find settings for the Enigma machine. Turing played a crucial role in cracking intercepted coded messages that enabled the Allies to defeat the Axis powers in many crucial engagements, including the Battle of the Atlantic.[11][12]
After the war, Turing worked at the National Physical Laboratory, where he designed the Automatic Computing Engine, one of the first designs for a stored-program computer. In 1948, Turing joined Max Newman's Computing Machine Laboratory, at the Victoria University of Manchester, where he helped develop the Manchester computers[13] and became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis[1] and predicted oscillating chemical reactions such as the Belousov–Zhabotinsky reaction, first observed in the 1960s. Despite these accomplishments, Turing was never fully recognised in Britain during his lifetime because much of his work was covered by the Official Secrets Act.[14]
Turing was prosecuted in 1952 for homosexual acts. He accepted hormone treatment with DES, a procedure commonly referred to as chemical castration, as an alternative to prison. Turing died on 7 June 1954, 16 days before his 42nd birthday, from cyanide poisoning. An inquest determined his death as a suicide, but it has been noted that the known evidence is also consistent with accidental poisoning. Following a public campaign in 2009, the British prime minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way [Turing] was treated". Queen Elizabeth II granted a posthumous pardon in 2013. The term "Alan Turing law" is now used informally to refer to a 2017 law in the United Kingdom that retroactively pardoned men cautioned or convicted under historical legislation that outlawed homosexual acts.[15]
Turing has an extensive legacy with statues of him and many things named after him, including an annual award for computer science innovations. He appears on the current Bank of England £50 note, which was released on 23 June 2021, to coincide with his birthday. A 2019 BBC series, as voted by the audience, named him the greatest person of the 20th century.
"""
    score = englishFreqMatchScore(myMessage)
    print(score)

if __name__ == '__main__':
    main()
