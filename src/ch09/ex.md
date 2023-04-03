Ex.1
```py
>>> import random
>>> random.seed(9)
>>> print(random.randint(1, 10))
8
>>> print(random.randint(1, 10))
10
>>> random.seed(9)
>>> print(random.randint(1, 10))
8
>>> print(random.randint(1, 10))
10
```


Ex.2
```py
>>> spam = [1, 2, 3]
>>> eggs = spam
>>> ham = eggs
>>> ham[0] = 99
>>> print(ham == spam)
True
>>> spam
[99, 2, 3]
>>> eggs
[99, 2, 3]
>>> ham
[99, 2, 3]
```


Ex.3
```py
>>> import copy
>>> spam1 = [1,2,3,4,5]
>>> spam2 = copy.deepcopy(spam1)
>>> spam1[0] = 88
>>> spam1
[88, 2, 3, 4, 5]
>>> spam2
[1, 2, 3, 4, 5]
```


Ex.4
```py
>>> import copy
>>> spam = [1,2]
>>> eggs = copy.deepcopy(spam)
>>> ham = copy.deepcopy(eggs)
>>> ham[0] = 99
>>> print(ham == spam)
False
>>> spam
[1, 2]
>>> eggs
[1, 2]
>>> ham
[99, 2]
```
