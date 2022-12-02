# Advent of Code - Day 2 - Part One

def result(input):
    res = 0
    for a, b in input:
        if (a == 'A' and b == 'Y') or (a == 'B' and b == 'Z') or (a == 'C' and b == 'X'):
            res += 6
        elif (a == 'A' and b == 'X') or (a == 'B' and b == 'Y') or (a == 'C' and b == 'Z'):
            res += 3
        if b == 'X':
            res += 1
        elif b == 'Y':
            res += 2
        else:
            res += 3
    return res
