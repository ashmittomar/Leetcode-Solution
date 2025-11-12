class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # fixed 'let' -> 'left'
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left


# ---- For user input ----
if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
    target = int(input("Enter the target number: "))
    
    obj = Solution()
    position = obj.searchInsert(nums, target)
    
    print(f"The target should be inserted at index: {position}")
