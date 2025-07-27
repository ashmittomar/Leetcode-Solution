from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

user_input = input("Enter words separated by spaces: ")

strs = user_input.strip().split()

result = group_anagrams(strs)
print("Grouped Anagrams:", result)
