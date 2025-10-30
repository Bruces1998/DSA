from heapq import heapify, heappush, heappushpop
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.small, -num)
            ele = heappop(self.small)
            heappush(self.large, -ele)
        
        else:
            heappush(self.large, num)
            ele = heappop(self.large)
            heappush(self.small, -ele)
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        
        else:
            return self.large[0]/1