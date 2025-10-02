class Solution(object):
    def isUgly(self, n):
        
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    sol = Solution()
    if sol.isUgly(n):
        print(f"{n} is an Ugly Number ✅")
    else:
        print(f"{n} is NOT an Ugly Number ❌")
