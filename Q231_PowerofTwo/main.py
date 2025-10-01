class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    result = Solution().isPowerOfTwo(n)
    print("Is power of two?", result)
