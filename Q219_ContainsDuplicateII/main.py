class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
       
        seen = {}  # stores number -> last index
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False



nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
k = int(input("Enter k: "))

sol = Solution()
print("Output:", sol.containsNearbyDuplicate(nums, k))
