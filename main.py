#!/usr/bin/env python

from tower import *
import constants as c

towers = {1: Tower(c.VOLUME), 2: Tower(), 3: Tower()}

def hanoi(n, i, j):
    if n == 1:
        towers[j].pushDisk(towers[i].popDisk())
    else:
        k = 6 - i - j
        hanoi(n-1, i, k)
        hanoi(1, i, j)
        hanoi(n-1, k, j)

def main():
    print(towers[1].tower, "\t", towers[3].tower)
    hanoi(c.VOLUME, 1, 3)
    print(towers[1].tower, "\t", towers[3].tower)

if __name__ == "__main__": main()
