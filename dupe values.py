
from collections import Counter

def find_duplicates(s):
    elements = Counter(s)
    return [k for k,v in elements.items() if v>1]
word=input("enter word : ")
print(find_duplicates(word))
wor=find_duplicates(word)
print(set(wor))
