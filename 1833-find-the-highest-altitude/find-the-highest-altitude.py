class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        preSum=0
        maxSum=0
        for i in gain:
            preSum+=i
            maxSum=max(maxSum, preSum)
        return maxSum