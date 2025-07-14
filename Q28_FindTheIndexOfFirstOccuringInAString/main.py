class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)

haystack = input("Enter the haystack string: ")
needle = input("Enter the needle string: ")

solution = Solution()
result = solution.strStr(haystack, needle)

print("First occurrence index:", result)
