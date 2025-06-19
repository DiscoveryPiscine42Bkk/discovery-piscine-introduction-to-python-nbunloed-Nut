import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + 'Z' * (8 - len(text)))

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)