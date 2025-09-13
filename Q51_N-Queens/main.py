class Solution(object):
    def solveNQueens(self, n):
        
        def backtrack(row, cols, diagonals, anti_diagonals, board):
            # If all queens are placed, save the solution
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                diag = row - col
                anti_diag = row + col

                if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)

                # Next row
                backtrack(row + 1, cols, diagonals, anti_diagonals, board)

                # Backtrack (remove queen)
                board[row][col] = "."
                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)

        result = []
        board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result



if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    solver = Solution()
    solutions = solver.solveNQueens(n)

    print("\nTotal Solutions:", len(solutions))
    for idx, sol in enumerate(solutions, 1):
        print(f"\nSolution {idx}:")
        for row in sol:
            print(row)
