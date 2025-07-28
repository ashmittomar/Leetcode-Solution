from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        return result

input_str = input("Enter distinct integers separated by commas: ")
nums = list(map(int, input_str.split(',')))

sol = Solution()
permutations = sol.permute(nums)

print("All possible permutations:")
for perm in permutations:
    print(perm)
