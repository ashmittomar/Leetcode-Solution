class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


nums = list(map(int, input("Enter numbers separated by space: ").split()))

sol = Solution()
print("Majority Element:", sol.majorityElement(nums))
