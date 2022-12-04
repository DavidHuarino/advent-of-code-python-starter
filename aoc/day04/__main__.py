#!/usr/bin/env python3

from pathlib import Path

from aoc.day04 import part1, part2

def read_file(filename):
    path = Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        lines = [strRanges.split(',') for strRanges in f.read().splitlines()]
        for i, subRange in enumerate(lines):
            temp = []
            for arr in subRange:
                a, b = arr.split('-')
                temp += [int(a), int(b)]
            lines[i] = temp
        return lines

def main():
    input = read_file("./resources/input.txt")

    print("--- Part One ---")
    print("Result:", part1.result(input))

    print("--- Part Two ---")
    print("Result:", part2.result(input))

if __name__ == "__main__":
    main()
