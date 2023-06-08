#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    n = len(argv)
    if n == 2:
        print("{} argument:".format(n - 1))
    elif n > 2:
        print("{} arguments:".format(n - 1))
    elif n == 1:
        print("{} arguments.".format(n - 1))
    for i in range(1, n):
        print("{}: {}".format(i, argv[i]))
