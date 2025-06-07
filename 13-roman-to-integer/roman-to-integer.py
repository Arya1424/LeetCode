class Solution(object):
    def romanToInt(self, s):
        total=0
        prev=0
        nums={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in s[::-1]:
            value=nums[i]
            if value<prev:
                total-=value
            else:
                total+=value
            prev=value
        return total

        