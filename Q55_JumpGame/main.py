class Solution(object):
    def canJump(self, nums):
       
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

input_str = input("Enter the array elements separated by spaces: ")
nums = list(map(int, input_str.strip().split()))

sol = Solution()
result = sol.canJump(nums)
print("Can reach the last index?" , result)
