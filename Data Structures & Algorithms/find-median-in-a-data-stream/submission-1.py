import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] 
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small, -num)
        elif num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) - len(self.large) > 1:
            moved = heapq.heappop(self.small)
            heapq.heappush(self.large, -moved)
        elif len(self.large) - len(self.small) > 1:
            moved = heapq.heappop(self.large)
            heapq.heappush(self.small, -moved)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            median = ((-self.small[0]) + (self.large[0])) / 2
        elif len(self.small) > len(self.large):
            median = -self.small[0]
        else:
            median = self.large[0]
        return median
        
        