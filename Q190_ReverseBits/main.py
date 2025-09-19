class Solution(object):
    def reverseBits(self, n):
       
        result = 0
        for i in range(32):
            result <<= 1         
            result |= (n & 1)    # copy the last bit  n
            n >>= 1              
        return result


if __name__ == "__main__":
    n = int(input("Enter a 32-bit signed integer: "))
    sol = Solution()
    print("Reversed bits integer:", sol.reverseBits(n))
