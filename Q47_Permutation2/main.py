class Solution(object):
    def permuteUnique(self, nums):
       
        result = []
        nums.sort()
        visited = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                result.append(list(path))
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                backtrack(path + [nums[i]])
                visited[i] = False

        backtrack([])
        return result

input_str = input("Enter integers (can include duplicates), separated by commas: ")
nums = list(map(int, input_str.strip().split(',')))

sol = Solution()
unique_permutations = sol.permuteUnique(nums)

print("\nAll unique permutations:")
for perm in unique_permutations:
    print(perm)
