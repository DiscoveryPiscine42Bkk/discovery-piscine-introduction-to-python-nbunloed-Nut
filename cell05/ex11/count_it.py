import sys

args = sys.argv[1:]

if len(args) == 0:
    print("$")
else:
    print(f"parameters: {len(args)}")
    for param in args:
        print(f"{param}: {len(param)}")