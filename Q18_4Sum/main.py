class solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result= []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n -1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right -1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total<target:
                        left += 1
                    else:
                        right -= 1
        return result


if __name__== "__main__":
    nums_input = input("Enter the numbers separated by spaces: ")
    nums = list(map(int, nums_input.strip().split()))
    target = int(input("Enter the target sum: "))

    solution = solution()
    result = solution.fourSum(nums, target)

    print("Unique quadruplets that sum to target: ")
    for quad in result:
        print(quad)





