import sys

if len(sys.argv) !=2:
    print("Nope, sorry...")
else:
    user_input = input("Enter a word: ")
    if user_input == sys.argv[1]:
        print("Good Jod!")
    else:
        print("Nope, sorry...")