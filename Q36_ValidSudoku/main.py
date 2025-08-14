class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                if num in rows[r] or num in cols[c] or num in boxes[(r // 3) * 3 + (c // 3)]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[(r // 3) * 3 + (c // 3)].add(num)

        return True


board = []
print("Enter the Sudoku board row by row.")
print("Use '.' for empty cells and separate numbers with spaces (e.g. '5 3 . . 7 . . . .')")

for i in range(9):
    while True:
        row = input(f"Row {i+1}: ").strip().split()
        if len(row) == 9 and all(x in "123456789." for x in row):
            board.append(row)
            break
        else:
            print("Invalid row. Please enter exactly 9 values using digits 1-9 or '.' for empty.")

sol = Solution()
if sol.isValidSudoku(board):
    print("The Sudoku board is valid.")
else:
    print("The Sudoku board is invalid.")
