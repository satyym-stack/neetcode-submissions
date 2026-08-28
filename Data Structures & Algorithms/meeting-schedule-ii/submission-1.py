"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        s, e = 0, 0
        room_in_use = 0
        meeting_room = 0

        while s != len(start):
            if start[s] < end[e]:
                room_in_use += 1
                s += 1
            else:
                room_in_use -= 1
                e += 1

            meeting_room = max(meeting_room, room_in_use)

        return meeting_room