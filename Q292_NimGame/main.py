class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0

n = int(input("Enter the number of stones: "))

obj = Solution()
result = obj.canWinNim(n)

if result:
    print("You can win the game!")
else:
    print("You will lose the game.")
