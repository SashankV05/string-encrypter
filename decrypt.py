print("welcome to decrypter")
p = input("enter the text you received in encrypter : ")
spl = p.split("?")
print(spl)
print("your id is " + spl[1])
id = spl[1]
word = spl[0]
print (id)

def split(word):
    return [char for char in word]


sp = split(word)
if id == "3":
    data = {'a': 'q', 'b': 'r', 'c': 's', 'd': 't', 'e': 'u', 'f': 'v', 'g': 'w', 'h': 'x', 'i': 'y', 'j': 'z',
            'k': 'a', 'l': 'b', 'm': 'c', 'n': 'd', 'o': 'e', 'p': 'f', 'q': 'g', 'r': 'h', 's': 'i', 't': 'j',
            'u': 'k', 'v': 'l', 'w': 'm', 'x': 'n', 'y': 'o', 'z': 'p'}
    l = sp
    s = set(l)
    fin=([data[x] for x in l])
    print (fin)
    listToStr = ''.join(map(str,fin))

    print(listToStr)
    ste = (listToStr)
    print("you entered = " + ste)
elif id == "2":
    data = {'a': 'l', 'b': 'm', 'c': 'n', 'd': 'o', 'e': 'p', 'f': 'q', 'g': 'r', 'h': 's', 'i': 't', 'j': 'u',
            'k': 'v', 'l': 'w', 'm': 'x', 'n': 'y', 'o': 'z', 'p': 'a', 'q': 'b', 'r': 'c', 's': 'd', 't': 'e',
            'u': 'f', 'v': 'g', 'w': 'h', 'x': 'i', 'y': 'j', 'z': 'k'},{'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y', 'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'}

    l = sp
    s = set(l)
    fin=([data[x] for x in l])
    print (fin)
    listToStr = ''.join(map(str,fin))

    print(listToStr)
    ste = (listToStr)
    print("you entered = " + ste)
elif id == "1":
    data = {'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o',
            'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y',
            'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e'}
    l = sp
    s = set(l)
    fin=([data[x] for x in l])
    print (fin)
    listToStr = ''.join(map(str,fin))

    print(listToStr)
    ste = (listToStr)
    print("you entered = "+ste)
elif id == "":
    print("you have entered wrong code")
    print("try again")
else:
    print("an error occured try again later")
