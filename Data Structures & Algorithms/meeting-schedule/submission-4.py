class Solution(object):
    def canAttendMeetings(self, intervals):

        if len(intervals) == 0:
            return True

        intervals.sort(key = lambda x: x.start)

        last_end = intervals[0].end

        for i in range (1, len(intervals)):
            current_start = intervals[i].start
            current_end = intervals[i].end

            if current_start < last_end:
                return False
            else:
                last_end = current_end

        return True