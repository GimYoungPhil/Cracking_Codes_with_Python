```py
>>> import simpleSubHacker
>>> import makeWordPatterns
>>> import wordPatterns
>>> letterMapping1 = simpleSubHacker.getBlankCipherletterMapping()
>>> letterMapping1
{'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}
>>> cipherWord = 'OLQIHXIRCKGNZ'
>>> pattern = makeWordPatterns.getWordPattern(cipherWord)
>>> pattern
'0.1.2.3.4.5.3.6.7.8.9.10.11'
>>> candidates = wordPatterns.allPatterns[pattern]
>>> candidates
['UNCOMFORTABLE', 'UNCOMFORTABLY']
>>> simpleSubHacker.addLettersToMapping(letterMapping1, cipherWord, candidates[0])
>>> letterMapping1
{'A': [], 'B': [], 'C': ['T'], 'D': [], 'E': [], 'F': [], 'G': ['B'], 'H': ['M'], 'I': ['O'], 'J': [], 'K': ['A'], 'L': ['N'], 'M': [], 'N': ['L'], 'O': ['U'], 'P': [], 'Q': ['C'], 'R': ['R'], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': ['F'], 'Y': [], 'Z': ['E']}
>>> simpleSubHacker.addLettersToMapping(letterMapping1, cipherWord, candidates[1])
>>> letterMapping1
{'A': [], 'B': [], 'C': ['T'], 'D': [], 'E': [], 'F': [], 'G': ['B'], 'H': ['M'], 'I': ['O'], 'J': [], 'K': ['A'], 'L': ['N'], 'M': [], 'N': ['L'], 'O': ['U'], 'P': [], 'Q': ['C'], 'R': ['R'], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': ['F'], 'Y': [], 'Z': ['E', 'Y']}
>>> 
```
