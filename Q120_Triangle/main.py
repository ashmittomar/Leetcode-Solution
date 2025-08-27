class Solution(object):
    def minimumTotal(self, triangle):
        
        # Bottom-up DP
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        return triangle[0][0]

#Input
if __name__ == "__main__":
    n = int(input("Enter number of rows in the triangle: "))
    triangle = []
    print("Enter the triangle values row by row:")
    for i in range(n):
        row = list(map(int, input().split()))
        triangle.append(row) 

    sol = Solution()
    result = sol.minimumTotal(triangle)
    print("Minimum path sum:", result)
