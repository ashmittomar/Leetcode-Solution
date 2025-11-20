class Solution(object):
    def removeDuplicates(self, nums):
       
        if not nums:
            return 0
        
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))
solution = Solution()
k = solution.removeDuplicates(nums)

print("Number of unique elements:", k)
print("Array after removing duplicates:", nums[:k])
