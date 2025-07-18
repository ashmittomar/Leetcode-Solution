class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            left = i+1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        

        return res

if __name__ == "__main__":
    user_input = input("Enter integers separated by space: ")
    nums = list(map(int, user_input.strip().split()))

    solution = Solution()
    result = solution.threeSum(nums)


    print("Unique triplets that sums to 0: ")
    print(result)