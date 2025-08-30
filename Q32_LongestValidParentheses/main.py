class Solution(object):
    def longestValidParentheses(self, s):
        
        stack = [-1]  # Base index
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len


if __name__ == "__main__":
    s = input("Enter a string of parentheses: ").strip()
    result = Solution().longestValidParentheses(s)
    print("Length of the longest valid parentheses substring:", result)
