import sys

def print_board_pretty(board_str):
    board_lines = board_str.strip().split('\n')
    size = len(board_lines)
    print("  +" + "---+" * size)
    for i, row in enumerate(board_lines):
        print(f"{size - i} | " + " | ".join(c if c != '.' else ' ' for c in row) + " |")
        print("  +" + "---+" * size)
    print("    " + "   ".join("ABCDEFGH"[:size]))

def checkmate(board_str, verbose=False):
    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    board_lines = board_str.strip().split('\n')
    size = len(board_lines)

    if any(len(row) != size for row in board_lines):
        print("Error")
        return

    board = [list(row) for row in board_lines]

    kings = [(i, j) for i in range(size) for j in range(size) if board[i][j] == 'K']
    if len(kings) != 1:
        print("Error")
        return

    xk, yk = kings[0]

    directions ={
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        'B': [(1, 1), (-1, -1), (1, -1), (-1, 1)],
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (-1, -1), (1, -1), (-1, 1)],
    }

    threat_count = 0

    for piece, dirs in directions.items():
        for dx, dy in dirs:
            x, y = xk + dx, yk + dy
            while in_bounds(x, y):
                if board[x][y] == '.':
                    x += dx
                    y += dy
                    continue
                elif board[x][y] == piece:
                    threat_count += 1
                    break
                else:
                    break
                
    for dx, dy in [(-1, -1), (-1, 1)]:
        x, y = xk + dx, yk + dy
        if in_bounds(x, y) and board[x][y] == 'P':
            threat_count += 1

    if verbose:
        print_board_pretty(board_str)
        print(f"Threats to King: {threat_count}")
    if threat_count > 0:
        print("Success")
    else:
        print("Fail")

def read_file(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return content
    except Exception:
        return None

def main():
    if len(sys.argv) < 2:
        print("Error")
        return

    for path in sys.argv[1:]:
        content = read_file(path)
        if content is None:
            print("Error")
        else:
            checkmate(content)

if __name__ == "__main__":
    main()
