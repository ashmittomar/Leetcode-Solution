class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Pointer for the position of unique elements
        k = 1

        # Loop through the array starting from index 1
        for i in range(1, len(nums)):
            # If current element is not equal to the previous unique one
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))
solution = Solution()
k = solution.removeDuplicates(nums)

print("Number of unique elements:", k)
print("Array after removing duplicates:", nums[:k])
