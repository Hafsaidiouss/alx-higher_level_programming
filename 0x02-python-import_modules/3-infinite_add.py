#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    n = len(argv)
    s = 0
    for i in range(1, n):
        s = s + int(argv[i])
    print("{}".format(s))
