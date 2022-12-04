# Advent of Code - Day 4 - Part Two

def result(input):
    res = 0
    for a, b, c, d in input:
        if a < c:
            if d <= b or a <= c <= b:
                res += 1
        elif a > c:
            if d >= b or c <= a <= d:
                res += 1
        else:
            res += 1
    return res
