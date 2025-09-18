class Solution(object):
    def convertToTitle(self, columnNumber):
        
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1   # adjust for 1-based indexing
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder))  # map to A-Z
            columnNumber //= 26
        
        return ''.join(reversed(result))


if __name__ == "__main__":
    num = int(input("Enter a column number: "))
    s = Solution()
    print("Excel Column Title:", s.convertToTitle(num))
