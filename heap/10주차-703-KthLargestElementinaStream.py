import heapq
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.bigs = []
        smalls = [-num for num in nums]
        heapq.heapify(smalls)
        for _ in range(k-1):
            num = -heapq.heappop(smalls)
            self.bigs.append(num)
        self.bigs.reverse()

        self.ans = -10**4-1
        if smalls:
            self.ans = -heapq.heappop(smalls)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if val > self.ans:
            self.ans = heapq.heappushpop(self.bigs, val)
        return self.ans

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)