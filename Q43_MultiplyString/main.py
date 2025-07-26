class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                result[i + j] += digit1 * digit2
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(str(d) for d in reversed(result))


if __name__ == "__main__":
    num1 = input("Enter first non-negative number: ")
    num2 = input("Enter second non-negative number: ")

    sol = Solution()
    product = sol.multiply(num1, num2)
    print("Product:", product)
