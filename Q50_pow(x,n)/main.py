def myPow(x, n):
    def fastPow(base, power):
        if power == 0:
            return 1.0
        half = fastPow(base, power // 2)
        if power % 2 == 0:
            return half * half
        else:
            return half * half * base

    if n < 0:
        x = 1 / x
        n = -n
    return fastPow(x, n)

try:
    x = float(input("Enter the base (x): "))
    n = int(input("Enter the exponent (n): "))
    result = myPow(x, n)
    print(f"{x}^{n} = {result:.5f}")
except ValueError:
    print("Invalid input. Please enter a valid float for x and integer for n.")
