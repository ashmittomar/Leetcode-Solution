def isValid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            return False  

    return not stack

user_input = input("Enter a string containing brackets: ")
print("Valid" if isValid(user_input) else "Invalid")
