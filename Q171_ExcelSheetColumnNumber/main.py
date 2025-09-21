class Solution(object):
    def titleToNumber(self, columnTitle):
        
        result = 0
        for char in columnTitle:
            num = ord(char) - ord('A') + 1
            result = result * 26 + num
        return result

columnTitle = input("Enter the Excel column title: ").upper() 
sol = Solution()
columnNumber = sol.titleToNumber(columnTitle)
print(f"The column number for '{columnTitle}' is: {columnNumber}")
