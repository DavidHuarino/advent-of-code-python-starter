# Advent of Code - Day 1 - Part Two

def result(input):
    return sum(sorted([sum(arr) for arr in input])[-3:])
