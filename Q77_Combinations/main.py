class Solution(object):
    def combine(self, n, k):
        
        result = []

        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result

if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    k = int(input("Enter value of k: "))

    solution = Solution()
    combinations = solution.combine(n, k)
    print("All combinations:")
    for combo in combinations:
        print(combo)
