class Solution(object):
    def nextPermutation(self, nums):
        
        # Step 1: Find first decreasing index from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If found, swap with next larger element
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse suffix
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1


nums = list(map(int, input("Enter numbers separated by space: ").split()))

sol = Solution()
sol.nextPermutation(nums)

print("Next permutation:", nums)
