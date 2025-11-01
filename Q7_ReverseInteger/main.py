class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_num = 0   # fixed variable name
        
        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10
            
            if (reversed_num > INT_MAX // 10 or
                (reversed_num == INT_MAX // 10 and digit > INT_MAX % 10)):
                return 0
            
            reversed_num = reversed_num * 10 + digit
        
        return sign * reversed_num


num = int(input("Enter an integer: "))
obj = Solution()
print("Reversed integer:", obj.reverse(num))
