class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        return x_str == x_str[::-1]

x = int(input("Enter a number: "))
print(Solution().isPalindrome(x))
