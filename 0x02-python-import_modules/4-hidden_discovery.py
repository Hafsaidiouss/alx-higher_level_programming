#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    ls = dir(hidden_4)
    ls.sort
    n = len(ls)
    for i in range(n):
        if ls[i][0:2] != "__":
            print("{}".format(ls[i]))
