class Solution(object):
    def isAnagram(self, s, t):
       
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


s = input("Enter first string (s): ")
t = input("Enter second string (t): ")

sol = Solution()
print("Output:", sol.isAnagram(s, t))
