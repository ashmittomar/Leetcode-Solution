class Solution(object):
    def removeDuplicates(self, nums):
       
        n = len(nums)
        if n <= 2:
            return n

        k = 2
        for i in range(2, n):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    nums = list(map(int, input("Enter the sorted array (space-separated): ").split()))
    
    solution = Solution()
    k = solution.removeDuplicates(nums)
    
    print("k =", k)
    print("Modified array:", nums[:k])
