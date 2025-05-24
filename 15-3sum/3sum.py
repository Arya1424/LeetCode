class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # sort once upfront
        result = []

        for i in range(len(nums)):
            # Skip duplicate values for i to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1  # Need a bigger sum, move left up
                else:
                    right -= 1  # Need a smaller sum, move right down

        return result
