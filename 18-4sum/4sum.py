class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Move both pointers and skip duplicates
                        left_val, right_val = nums[left], nums[right]
                        while left < right and nums[left] == left_val:
                            left += 1
                        while left < right and nums[right] == right_val:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
