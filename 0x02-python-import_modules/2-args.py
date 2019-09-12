#!/usr/bin/python3
import sys

argc = len(sys.argv)
i = 1

if argc == 1:
    print("0 arguments.")
elif argc == 2:
    print("1 argument:")
else:
    print("{} arguments".format(argc))

for arg in sys.argv[1:]:
    print("{}: {}".format(i, arg))
    i += 1
