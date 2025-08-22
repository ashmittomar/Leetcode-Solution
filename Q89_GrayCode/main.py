class Solution(object):
    def grayCode(self, n):
        
        res = []
        for i in range(1 << n):   
            res.append(i ^ (i >> 1))
        return res

if __name__ == "__main__":
    n = int(input("Enter n: "))
    s = Solution()
    print("Gray code sequence:", s.grayCode(n))
