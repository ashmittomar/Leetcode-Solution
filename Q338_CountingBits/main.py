class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            ans.append(bin(i).count('1'))
        return ans

n = int(input("Enter a number: "))

obj = Solution()
result = obj.countBits(n)

print("Output:", result)
