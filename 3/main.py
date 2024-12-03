#!/usr/bin/env python3
import re

with open("input.txt") as file:
    input = file.read()

SAMPLE = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
SAMPLE2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def double_split(input, parse_func=lambda x: x):
    groups = input.split("\n\n")
    return [parse_func(x) for x in groups]


def parse(line):
    return line


def solve1(input):
    instructions = re.findall(r'mul\([0-9]+,[0-9]+\)', input)
    # print(instructions)

    sum = 0
    for i in instructions:
        nums = re.findall(r'[0-9]+', i)
        sum += (int(nums[0]) * int(nums[1]))

    return sum


def solve2(input):
    instructions = re.findall(r'((mul\([0-9]+,[0-9]+\))|(do(n\'t)*\(\)))', input)

    sum = 0
    enabled = True
    for m in instructions:
        i = m[0]
        # print(i)

        if i == "don't()":
            enabled = False
            continue
        elif i == 'do()':
            enabled = True
            continue

        if enabled:
            nums = re.findall(r'[0-9]+', i)
            sum += (int(nums[0]) * int(nums[1]))

    return sum


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 161
    assert solve2(SAMPLE2) == 48

    # Part 1
    part1 = solve1(input)
    assert part1 == 184511516
    print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 90044227
    print(part2)
