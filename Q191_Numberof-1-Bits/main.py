class Solution(object):
    def hammingWeight(self, n):
        
        return bin(n).count('1')


if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    s = Solution()
    print("Number of set bits:", s.hammingWeight(n))
