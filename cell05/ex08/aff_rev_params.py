import sys

if len(sys.argv) < 3:
    print("three two one")
else:
    for param in reversed(sys.argv[1:]):
        print(param)