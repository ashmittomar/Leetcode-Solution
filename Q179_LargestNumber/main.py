from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == "0":
            return "0"
        return ''.join(nums)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(Solution().largestNumber(nums))
