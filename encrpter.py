import random


def split(word):
    return [char for char in word]


ids = ("120-1-090", "900-2-001", "220-100-011")
id = random.choice(ids)
word = input("enter the word :")
spw = (split(word))

print(spw)
if id == "120-1-090":  # shiftdict21

    data = {'a': 'v', 'b': 'w', 'c': 'x', 'd': 'y', 'e': 'z', 'f': 'a', 'g': 'b', 'h': 'c', 'i': 'd', 'j': 'e',
            'k': 'f', 'l': 'g', 'm': 'h', 'n': 'i', 'o': 'j', 'p': 'k', 'q': 'l', 'r': 'm', 's': 'n', 't': 'o',
            'u': 'p', 'v': 'q', 'w': 'r', 'x': 's', 'y': 't', 'z': 'u'}, \
           {'A': 'V', 'B': 'W', 'C': 'X', 'D': 'Y', 'E': 'Z', 'F': 'A', 'G': 'B', 'H': 'C', 'I': 'D', 'J': 'E',
            'K': 'F', 'L': 'G', 'M': 'H', 'N': 'I', 'O': 'J', 'P': 'K', 'Q': 'L', 'R': 'M', 'S': 'N', 'T': 'O',
            'U': 'P', 'V': 'Q', 'W': 'R', 'X': 'S', 'Y': 'T', 'Z': 'U'}

    s = set(spw)
    enc = ([data[x] for x in spw])
    print(enc)
    listToStr = ''.join(map(str, enc))

    print(listToStr)
    ste = (listToStr)
    print("paste this in decrypter")
    print(ste + "?1")

elif id == "900-2-001":  # shiftdict15
    data1 = {'a': 'p', 'b': 'q', 'c': 'r', 'd': 's', 'e': 't', 'f': 'u', 'g': 'v', 'h': 'w', 'i': 'x', 'j': 'y',
             'k': 'z', 'l': 'a', 'm': 'b', 'n': 'c', 'o': 'd', 'p': 'e', 'q': 'f', 'r': 'g', 's': 'h', 't': 'i',
             'u': 'j', 'v': 'k', 'w': 'l', 'x': 'm', 'y': 'n', 'z': 'o'}
    s = set(spw)
    enc = ([data1[x] for x in spw])
    print(enc)
    print("paste this in decrypter")
    listToStr = ''.join(map(str, enc))

    print(listToStr)
    ste = (listToStr)
    print(ste + "?" + "2")
elif id == "220-100-011":  # shiftdict10
    data2 = {'a': 'k', 'b': 'l', 'c': 'm', 'd': 'n', 'e': 'o', 'f': 'p', 'g': 'q', 'h': 'r', 'i': 's', 'j': 't',
             'k': 'u', 'l': 'v', 'm': 'w', 'n': 'x', 'o': 'y', 'p': 'z', 'q': 'a', 'r': 'b', 's': 'c', 't': 'd',
             'u': 'e', 'v': 'f', 'w': 'g', 'x': 'h', 'y': 'i', 'z': 'j'}
    s = set(spw)
    enc = ([data2[x] for x in spw])
    print(enc)
    print("paste this in decrypter")
    listToStr = ''.join(map(str, enc))

    print(listToStr)
    ste = (listToStr)
    print(ste + "?" + "3")
