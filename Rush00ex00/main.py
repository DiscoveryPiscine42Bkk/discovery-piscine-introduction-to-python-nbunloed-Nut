import sys
from checkmate import checkmate

def read_board(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = [line.rstrip('\n') for line in f if line.strip()]
            size = len(lines)
            if any(len(row) != size for row in lines):  
                return None
            return '\n'.join(lines)
    except:
        return None

def main():
    if len(sys.argv) < 2:
        return

    for file_path in sys.argv[1:]:
        board_str = read_board(file_path)
        if board_str is None:
            print("Error")
        else:
            checkmate(board_str)

if __name__ == "__main__":
    main()
