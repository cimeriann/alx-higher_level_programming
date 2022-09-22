#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    if (len(argv)-1) >= 2:
        print("{:d} arguments:".format(len(argv)-1))
        while i < len(argv):
            print("{:d}: {}".format(i, argv[i]))
            i += 1
    elif (len(argv)-1) == 0:
        print("{:d} arguments.".format(len(argv)-1))
    else:
        print("{:d} argument:".format(len(argv)-1))
        print("{:d}: {}".format(i, argv[i]))
