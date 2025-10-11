class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


user_input = input("Enter the numbers separated by spaces: ")
nums = list(map(int, user_input.split()))

solution = Solution()
missing = solution.missingNumber(nums)
print("The missing number is:", missing)
