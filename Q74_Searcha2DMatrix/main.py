class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    matrix = []
    print("Enter matrix row by row (space-separated):")
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    target = int(input("Enter target: "))

    s = Solution()
    result = s.searchMatrix(matrix, target)
    print("Output:", result)
