class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0], reverse = True)
        ans = []
        while len(intervals) >= 2:
            i1 = intervals.pop()
            i2 = intervals[-1]
            s1, e1 = i1
            s2, e2 = i2
            if e1 >= s2:
                intervals.pop()
                intervals.append([s1, max(e1, e2)])
            else:
                ans.append([s1, e1])
        ans.append(intervals[-1])
        
        return ans