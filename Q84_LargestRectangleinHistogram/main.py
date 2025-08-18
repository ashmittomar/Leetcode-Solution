class Solution(object):
    def largestRectangleArea(self, heights):
      
        stack = []  # stores indices of bars
        max_area = 0
        heights.append(0)  # sentinel to pop all remaining bars

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area


if __name__ == "__main__":
    heights = list(map(int, input("Enter bar heights separated by spaces: ").split()))
    sol = Solution()
    print("Largest Rectangle Area:", sol.largestRectangleArea(heights))
