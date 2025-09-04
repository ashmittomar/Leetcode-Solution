class Solution(object):
    def solve(self, board):
        
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "#"  # mark safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: mark border-connected regions
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)

        # Step 2: flip and restore
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"


if __name__ == "__main__":
    m, n = map(int, input("Enter rows and cols: ").split())
    print("Enter the board row by row (characters X or O without spaces):")
    board = []
    for _ in range(m):
        row = list(input().strip())
        board.append(row)

    sol = Solution()
    sol.solve(board)

    print("\nFinal board:")
    for row in board:
        print("".join(row))
