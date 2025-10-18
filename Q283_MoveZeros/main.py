class Solution(object):
    def moveZeroes(self, nums):
        last_non_zero = 0  
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap non-zero element to the correct position
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1


nums = list(map(int, input("Enter numbers separated by space: ").split()))

obj = Solution()
obj.moveZeroes(nums)

print("Output:", nums)
