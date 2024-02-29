# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

import re
class NestedIterator(object):

    idx = -1
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.arr = []
        def initializearr(nestedarr):
            if nestedarr.isInteger():
                self.arr.append(nestedarr.getInteger())
            else:
                arr = nestedarr.getList()
                for a in arr:
                    initializearr(a)

        for arr in nestedList:
            initializearr(arr)

    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.arr[self.idx]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.arr)-1

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())