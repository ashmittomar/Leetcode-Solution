class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # Create prefix sum array
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right + 1] - self.prefix[left]


nums = list(map(int, input("Enter array elements (space-separated): ").split()))

# Create NumArray object
numArray = NumArray(nums)

# Take number of queries
q = int(input("Enter number of queries: "))

for i in range(q):
    left, right = map(int, input(f"Enter left and right index for query {i+1}: ").split())
    print(f"Sum of elements from index {left} to {right} =", numArray.sumRange(left, right))
