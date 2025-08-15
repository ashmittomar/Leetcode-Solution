class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:  # Red
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # White
                mid += 1
            else:  # Blue
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements (0=Red, 1=White, 2=Blue) separated by space: ").split()))

solution = Solution()
solution.sortColors(nums)

print("Sorted colors:", nums)
