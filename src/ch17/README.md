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

>>> letterMapping2 = simpleSubHacker.getBlankCipherletterMapping()
>>> cipherWord = 'PLQRZKBZB'
>>> pattern = makeWordPatterns.getWordPattern(cipherWord)
>>> pattern
'0.1.2.3.4.5.6.4.6'
>>> candidates = wordPatterns.allPatterns[pattern]
>>> candidates
['CONVERSES', 'INCREASES', 'PORTENDED', 'UNIVERSES']

>>> for candidate in candidates:
	simpleSubHacker.addLettersToMapping(letterMapping2, cipherWord, candidate)
	
>>> letterMapping2
{'A': [], 'B': ['S', 'D'], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': ['R', 'A', 'N'], 'L': ['O', 'N'], 'M': [], 'N': [], 'O': [], 'P': ['C', 'I', 'P', 'U'], 'Q': ['N', 'C', 'R', 'I'], 'R': ['V', 'R', 'T'], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': ['E']}

>>> intersectedMapping = simpleSubHacker.intersectMappings(letterMapping1, letterMapping2)
>>> intersectedMapping
{'A': [], 'B': ['S', 'D'], 'C': ['T'], 'D': [], 'E': [], 'F': [], 'G': ['B'], 'H': ['M'], 'I': ['O'], 'J': [], 'K': ['A'], 'L': ['N'], 'M': [], 'N': ['L'], 'O': ['U'], 'P': ['C', 'I', 'P', 'U'], 'Q': ['C'], 'R': ['R'], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': ['F'], 'Y': [], 'Z': ['E']}

>>> letterMapping3 = simpleSubHacker.getBlankCipherletterMapping()
>>> cipherWord = 'MPBKSSIPLC'
>>> pattern = makeWordPatterns.getWordPattern(cipherWord)
>>> pattern
'0.1.2.3.4.4.5.1.6.7'
>>> candidates = wordPatterns.allPatterns[pattern]
>>> candidates
['ADMITTEDLY', 'DISAPPOINT']

>>> for candidate in candidates:
	simpleSubHacker.addLettersToMapping(letterMapping3, cipherWord, candidate)
	
>>> letterMapping3
{'A': [], 'B': ['M', 'S'], 'C': ['Y', 'T'], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': ['E', 'O'], 'J': [], 'K': ['I', 'A'], 'L': ['L', 'N'], 'M': ['A', 'D'], 'N': [], 'O': [], 'P': ['D', 'I'], 'Q': [], 'R': [], 'S': ['T', 'P'], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

>>> intersectedMapping = simpleSubHacker.intersectMappings(intersectedMapping, letterMapping3)
>>> intersectedMapping
{'A': [], 'B': ['S'], 'C': ['T'], 'D': [], 'E': [], 'F': [], 'G': ['B'], 'H': ['M'], 'I': ['O'], 'J': [], 'K': ['A'], 'L': ['N'], 'M': ['A', 'D'], 'N': ['L'], 'O': ['U'], 'P': ['I'], 'Q': ['C'], 'R': ['R'], 'S': ['T', 'P'], 'T': [], 'U': [], 'V': [], 'W': [], 'X': ['F'], 'Y': [], 'Z': ['E']}

>>> simpleSubHacker.removeSolvedLettersFromMapping(intersectedMapping)
>>> intersectedMapping
{'A': [], 'B': ['S'], 'C': ['T'], 'D': [], 'E': [], 'F': [], 'G': ['B'], 'H': ['M'], 'I': ['O'], 'J': [], 'K': ['A'], 'L': ['N'], 'M': ['D'], 'N': ['L'], 'O': ['U'], 'P': ['I'], 'Q': ['C'], 'R': ['R'], 'S': ['P'], 'T': [], 'U': [], 'V': [], 'W': [], 'X': ['F'], 'Y': [], 'Z': ['E']}
```
