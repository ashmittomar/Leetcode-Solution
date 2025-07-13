class Solution:
    def removeElement(self, nums, val):
        k = 0  # Pointer for the next position of a non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# === User Input Section ===
nums = list(map(int, input("Enter the list of numbers separated by space: ").split()))
val = int(input("Enter the value to remove: "))

# === Processing ===
solution = Solution()
k = solution.removeElement(nums, val)

# === Output ===
print("\nNumber of elements not equal to", val, ":", k)
print("Updated list (first", k, "elements):", nums[:k])
