def get_next(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit * digit
        number //= 10
    return total

def is_happy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = get_next(n)
    return True


n = int(input("Enter a number: "))
if is_happy(n):
    print(n, "is a Happy Number")
else:
    print(n, "is NOT a Happy Number")
