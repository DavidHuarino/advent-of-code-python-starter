# Advent of Code - Day 3 - Part One
import time
def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print(time.time() - inicio)
        return c
    return funcion_medida
@mide_tiempo    
def result(input):
    res = 0
    for word in input:
        sizeWord = len(word)
        firstPart = set(word[:sizeWord // 2])
        secondPart = set(word[sizeWord // 2:])
        sharedCharacter = firstPart & secondPart
        char = ''.join(sharedCharacter)
        if 'a' <= char <= 'z':
            res += (ord(char) - 97) % 26 + 1
        else:
            res += (ord(char) - 65) % 26 + 27
    return res
