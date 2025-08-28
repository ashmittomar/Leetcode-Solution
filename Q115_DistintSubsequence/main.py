class Solution(object):
    def numDistinct(self, s, t):
       
        m, n = len(s), len(t)
        
        # dp[i][j] = number of subsequences of s[:i] that equal t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty t can always be formed
        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]


if __name__ == "__main__":
    s = input("Enter string s: ")
    t = input("Enter string t: ")
    sol = Solution()
    print("Number of distinct subsequences:", sol.numDistinct(s, t))
