class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

nums1_input = input("Enter nums1 elements separated by space (including trailing zeros): ")
nums1 = list(map(int, nums1_input.strip().split()))
m = int(input("Enter number of initialized elements in nums1 (m): "))

nums2_input = input("Enter nums2 elements separated by space: ")
nums2 = list(map(int, nums2_input.strip().split()))
n = int(input("Enter number of initialized elements in nums2 (n): "))

sol = Solution()
sol.merge(nums1, m, nums2, n)

print("Merged nums1:", nums1)
