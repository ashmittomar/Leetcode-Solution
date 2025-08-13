class Solution(object):
    def subsets(self, nums):
        
        res = []

        def backtrack(start, path):
            res.append(list(path))
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


nums = list(map(int, input("Enter numbers separated by space: ").split()))

solution = Solution()
result = solution.subsets(nums)

print("All subsets (power set):")
for subset in result:
    print(subset)
