# Advent of Code - Day 5 - Part One
import copy
def result(input):
    copyarr = copy.deepcopy(input)
    stack, moves = copyarr
    for a, b, c in moves:
        int_a, int_b, int_c = int(a), int(b), int(c)
        while int_a > 0:
            popElement = stack[int_b - 1].pop()
            stack[int_c - 1].append(popElement)
            int_a -= 1
    return ''.join([arr[-1] for arr in stack])
