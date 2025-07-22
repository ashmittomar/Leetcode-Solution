class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        for i in reversed(range(n)):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + [0] * n

if __name__ == "__main__":
    user_input = input("Enter digits separated by spaces (e.g., 1 2 3): ")
    digits = list(map(int, user_input.strip().split()))
    
    sol = Solution()
    result = sol.plusOne(digits)
    
    print("Result after adding one:", result)
