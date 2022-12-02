# Advent of Code - Day 2 - Part Two

def result(input):
    res = 0
    for a, b in input:
        if b == 'Z':
            if a == 'A':
                res += 2
            elif a == 'B':
                res += 3
            else:
                res += 1
            res += 6
        elif b == 'Y':
            if a == 'A':
                res += 1
            elif a == 'B':
                res += 2
            else:
                res += 3
            res += 3
        else:
            if a == 'A':
                res += 3
            elif a == 'B':
                res += 1
            else:
                res += 2
    return res
