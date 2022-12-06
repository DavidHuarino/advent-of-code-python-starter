# Advent of Code - Day 6 - Part Two
from collections import defaultdict
def result(input):
    seen = defaultdict(int)
    start = 0
    for end, char in enumerate(input):
        seen[char] += 1
        if end - start + 1 > 14:
            seen[input[start]] -= 1
            if seen[input[start]] == 0:
                del seen[input[start]]
            start += 1
        if end - start + 1 == 14 and len(seen) == 14:
            return end + 1