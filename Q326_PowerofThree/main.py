class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

n = int(input("Enter an integer: "))

sol = Solution()
if sol.isPowerOfThree(n):
    print(f"{n} is a power of 3.")
else:
    print(f"{n} is NOT a power of 3.")
