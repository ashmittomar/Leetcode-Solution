class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


input_str = input("Enter heights separated by spaces: ")
height_list = list(map(int, input_str.strip().split()))

solution = Solution()
result = solution.maxArea(height_list)
print("Maximum water that can be contained:", result)
