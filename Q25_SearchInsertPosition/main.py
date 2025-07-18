class Solution(object):
    def searchInsert(self, nums, target):
        left, right= 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted distinct integers (space-separated): ").split()))
    target = int(input("Enter the target value: "))

    sol = Solution()
    index = sol.searchInsert(nums, target)
    print("Output index: ", index)