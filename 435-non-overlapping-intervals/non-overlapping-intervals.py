class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        overlap = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                overlap += 1
            else:
                prev_end = intervals[i][1]

        return overlap
