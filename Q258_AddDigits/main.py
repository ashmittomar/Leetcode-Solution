class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

num = int(input("Enter a number: "))
sol = Solution()
print("Result:", sol.addDigits(num))
