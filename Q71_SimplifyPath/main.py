def simplify_path(path):
    stack = []
    components = path.split('/')

    for part in components:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return '/' + '/'.join(stack)

if __name__ == "__main__":
    user_input = input("Enter a Unix-style path: ")
    result = simplify_path(user_input)
    print("Simplified canonical path:", result)
