class Solution(object):
    def findSubstring(self, s, words):
       
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = {}

        # Build frequency map of words
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        result = []

        # We need to try starting at different offsets
        for i in range(word_len):
            left = i
            right = i
            current_count = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1

                    # If frequency exceeds, move left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    # If all words match
                    if count == len(words):
                        result.append(left)
                else:
                    current_count.clear()
                    count = 0
                    left = right

        return result

\
if __name__ == "__main__":
    s = input("Enter the main string s: ")
    words = input("Enter the words (space separated): ").split()

    sol = Solution()
    result = sol.findSubstring(s, words)
    print("Starting indices of concatenated substrings:", result)
