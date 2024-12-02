#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def double_split(input, parse_func=lambda x: x):
    groups = input.split("\n\n")
    return [parse_func(x) for x in groups]


def parse(line):
    return [int(n) for n in line.split(' ')]


def issafe(line):
    isinc = None
    n0 = None
    for n in line:
        if n0 is not None:
            if n == n0:
                return False
            elif n > n0:  # increasing
                if isinc is False:
                    return False
                isinc = True
            else:  # decreasing
                if isinc is True:
                    return False
                isinc = False

            if abs(n - n0) > 3:
                return False
        n0 = n
    return True


def solve1(input):
    count = 0
    for line in input_split(input):
        r = parse(line)

        if issafe(r):
            count += 1

    return count


def solve2(input):
    count = 0
    for line in input_split(input):
        r = parse(line)

        if issafe(r):
            count += 1
        else:
            for idx, _ in enumerate(r):
                if issafe(r[:idx] + r[idx+1:]):
                    count += 1
                    break

    return count


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 2
    assert solve2(SAMPLE) == 4

    # Part 1
    part1 = solve1(input)
    assert part1 == 606
    print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 644
    print(part2)
