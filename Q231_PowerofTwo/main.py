class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0


# ---- User input part ----
if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    result = Solution().isPowerOfTwo(n)
    print("Is power of two?", result)
