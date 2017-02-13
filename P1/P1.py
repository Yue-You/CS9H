#!/usr/bin/env python
import sys


def print_row(row):
    output = ""
    for pixel in range(len(row)):
        output += str(row[pixel])
    print(output)


def main(argv):
    rules = int(argv[0])
    steps = int(argv[1])
    row = []
    for _ in range(steps):
        row.append(0)
    row.append(1)
    for _ in range(steps):
        row.append(0)
    width = len(row)
    print("P1 %d %d" % (width, steps + 1))
    print_row(row)
    rule = [int(x) for x in bin(rules)[2:]]
    while len(rule) < 8:
        rule.insert(0, 0)
    for _ in range(steps):
        new_row = []
        for index in range(width):
            neighbour = 0
            if index > 0:
                neighbour += row[index - 1] * 4
            neighbour += row[index] * 2
            if index < width - 1:
                neighbour += row[index + 1]
            new_row.append(rule[7 - neighbour])
        row = new_row
        print_row(row)

if __name__ == '__main__':
    main(sys.argv[1:])
