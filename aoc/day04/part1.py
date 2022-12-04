# Advent of Code - Day 4 - Part One

def result(input):
    res = 0
    for a, b, c, d in input:
        if a < c:
            if d <= b:
                res += 1
        elif a > c:
            if d >= b:
                res += 1
        else:
            res += 1
    return res
