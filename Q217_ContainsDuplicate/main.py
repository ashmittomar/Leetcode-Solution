class Solution(object):
    def containsDuplicate(self, nums):
        
        # Efficient set-based solution
        return len(nums) != len(set(nums))

nums = list(map(int, input("Enter integers separated by spaces: ").split()))

sol = Solution()
print(sol.containsDuplicate(nums))
