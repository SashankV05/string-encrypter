import random
def split(word):
    return [char for char in word]
import itertools
it = itertools.repeat()
word=input("enter the word :" )
x=(split(word))
data = {'a': 'v', 'b': 'w', 'c': 'x', 'd': 'y', 'e': 'z', 'f': 'a', 'g': 'b', 'h': 'c', 'i': 'd', 'j': 'e', 'k': 'f',
        'l': 'g', 'm': 'h', 'n': 'i', 'o': 'j', 'p': 'k', 'q': 'l', 'r': 'm', 's': 'n', 't': 'o', 'u': 'p', 'v': 'q',
        'w': 'r', 'x': 's', 'y': 't', 'z': 'u'}
s = set(x)
enc = ([v for k, v in data.items() if k in s])
print(enc)