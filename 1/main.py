#!/usr/bin/env python3
from collections import Counter

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def double_split(input, parse_func=lambda x: x):
    groups = input.split("\n\n")
    return [parse_func(x) for x in groups]


def parse(line):
    return line.split('   ')


def solve1(input):
    l1 = []
    l2 = []
    for line in input_split(input):
        n = parse(line)
        l1.append(int(n[0]))
        l2.append(int(n[1]))
    
    l1.sort()
    l2.sort()

    delta = 0
    for idx, _ in enumerate(l1):
        delta += abs(l1[idx] - l2[idx])

    return delta


def solve2(input):
    l1 = []
    l2 = []
    for line in input_split(input):
        n = parse(line)
        l1.append(int(n[0]))
        l2.append(int(n[1]))

    l1.sort()
    l2.sort()

    c2 = Counter(l2)

    score = 0
    for n in l1:
        score += n * c2[n]

    return score


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 11
    assert solve2(SAMPLE) == 31

    # Part 1
    part1 = solve1(input)
    assert part1 == 3714264
    print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 18805872
    print(part2)
