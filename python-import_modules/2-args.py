#!/usr/bin/python3
if __name__ == "__main__":
   from sys import argv
    args = len(argv) - 1
    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(args))
    for count in range(args):
        print("{:d}: {:d}".format(count + 1, sys.argv[count + 1]))
