class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i]) 
                path.pop()

        backtrack(0, [], 0)
        return res

candidates = list(map(int, input("Enter distinct candidate numbers (space-separated): ").split()))
target = int(input("Enter target value: "))

sol = Solution()
result = sol.combinationSum(candidates, target)
print("Combinations that sum to target:")
print(result)
