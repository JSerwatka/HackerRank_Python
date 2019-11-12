#!/bin/python3

from collections import Counter

if __name__ == '__main__':
    s = input()
    counted_letters = list(Counter(s).items())
    sorted_letters = sorted(counted_letters, reverse = False, key = lambda i: (-i[1], i[0]))[:3]

    for i in sorted_letters:
        print(*i)
