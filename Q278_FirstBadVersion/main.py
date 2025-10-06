def isBadVersion(version):
    return version >= bad

class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

n = int(input("Enter total number of versions: "))
bad = int(input("Enter the first bad version: "))
#y
obj = Solution()
print("The first bad version is:", obj.firstBadVersion(n))
