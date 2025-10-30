class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        max_length = 0
        start = 0

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_length = max(max_length, i - start + 1)
        
        return max_length


s = input("Enter a string: ")
sol = Solution()
print("Length of longest substring without repeating characters:", sol.lengthOfLongestSubstring(s))
