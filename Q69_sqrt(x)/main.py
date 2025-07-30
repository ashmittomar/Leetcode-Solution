class Solution(object):
    def mySqrt(self, x):
        
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

x = int(input("Enter a non-negative integer: "))
solution = Solution()
result = solution.mySqrt(x)
print("The square root (rounded down) is:", result)
