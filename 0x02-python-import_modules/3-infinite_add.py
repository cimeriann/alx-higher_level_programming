#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    result = 0
    if len(argv) > 1:
        for num in range(len(argv)-1):
            result += int(argv[i])
            i += 1
    print(result)
