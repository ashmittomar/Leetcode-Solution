def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def uniquePaths(m, n):
    return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))

m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

print("Number of unique paths:", uniquePaths(m, n))
