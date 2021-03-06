def shiftDict(i):
    i = i % 26
    alpha = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print( dict(zip(alpha,alpha[i:] + alpha[:i])))

shiftDict(5)