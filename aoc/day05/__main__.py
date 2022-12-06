#!/usr/bin/env python3

from pathlib import Path

from aoc.day05 import part1, part2

import copy

def read_file(filename):
    path = Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        lines = f.read().splitlines()
        charIndex = lines.index('')
        columns, moves = lines[:charIndex], lines[charIndex + 1:]
        strStack, listStacks = columns[:-1], columns[-1]
        numberStacks = int(listStacks.strip()[-1])
        stacks = [[] for _ in range(numberStacks)]
        for word in strStack:
            indexStack = 0
            for j in range(0, len(word), 4):
                if word[j + 1].strip():
                    stacks[indexStack].insert(0, word[j + 1])
                indexStack += 1
        movesStack = []
        for word in moves:
            _, movesNumber, _, start, _, end = word.split(' ') 
            movesStack.append([movesNumber, start, end])

        return [stacks, movesStack]

def main():
    input = read_file("./resources/input.txt")

    # newCopy = copy.deepcopy(input)

    print("--- Part One ---")
    print("Result:", part1.result(input))

    print("--- Part Two ---")
    print("Result:", part2.result(input))

if __name__ == "__main__":
    main()
