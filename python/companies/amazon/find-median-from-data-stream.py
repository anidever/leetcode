import heapq


class MedianFinder:

    def __init__(self):
        self.smalls = []
        heapq.heapify(self.smalls)
        # max heap
        self.bigs = []
        heapq.heapify(self.bigs)
        # min heap

    def addNum(self, num: int) -> None:
        if self.bigs and num > self.bigs[0]:
            heapq.heappush(self.bigs, num)
        else:
            heapq.heappush(self.smalls, -num)

        # Balance the heaps
        if len(self.smalls) > len(self.bigs) + 1:
            # if smalls has more than 1 element than bigs
            # pop the top element from smalls and push it to bigs
            value = -1 * heapq.heappop(self.smalls)
            heapq.heappush(self.bigs, value)
        elif len(self.bigs) > len(self.smalls):
            # if bigs has more than 1 element than smalls
            # pop the top element from bigs and push it to smalls
            value = heapq.heappop(self.bigs)
            heapq.heappush(self.smalls, -value)

    def findMedian(self) -> float:
        smalls_size = len(self.smalls)
        bigs_size = len(self.bigs)
        if smalls_size == bigs_size:
            return (-1 * self.smalls[0] + self.bigs[0]) / 2
        elif smalls_size > bigs_size:
            return -1 * self.smalls[0]
        else:
            return self.bigs[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()