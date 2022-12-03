# Advent of Code - Day 3 - Part Two
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
    count = 1
    arr = []
    for word in input:
        arr.append(word)
        if count % 3 == 0:
            a, b, c = arr
            sharedchar = set(a) & set(b) & set(c)
            char = ''.join(sharedchar)
            if 'a' <= char <= 'z':
                res += (ord(char) - 97) % 26 + 1
            else:
                res += (ord(char) - 65) % 26 + 27
            count = 0
            arr = []
        count += 1
    return res

