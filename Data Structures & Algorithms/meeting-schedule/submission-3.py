"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_meetings = sorted(intervals, key=lambda meeting: meeting.start)

        for i in range(len(sorted_meetings) - 1):

            current_end = sorted_meetings[i].end
            next_start = sorted_meetings[i + 1].start

            if current_end > next_start:
                return False

        return True