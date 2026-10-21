class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        n = len(intervals)

        intervals.sort(key = lambda x: x[0])

        res = 0
        last_end = intervals[0][1]

        for i in range (1,n):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            if current_start >= last_end:
                last_end = current_end
            else:
                res += 1
                last_end = min(last_end, current_end)

        return res
        