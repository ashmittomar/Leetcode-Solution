class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    sol = Solution()
    print("Single number is:", sol.singleNumber(nums))
