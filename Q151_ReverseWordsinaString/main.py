class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

s = input()
print(Solution().reverseWords(s))
