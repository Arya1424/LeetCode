class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res
