class Solution(object):
    def twoSum(self, nums, target):
        
        num_map = {}  # dictionary to store number -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


if __name__ == "__main__":
    nums = list(map(int, input("Enter the numbers separated by space: ").split()))
    target = int(input("Enter the target: "))

    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Indices of numbers that add up to target:", result)
