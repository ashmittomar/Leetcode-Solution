def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]


    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

user_input = input("Enter string separated by space: ")
strs = user_input.split()


result = longestCommonPrefix(strs)
print("Longest Common Prefix: ", result)