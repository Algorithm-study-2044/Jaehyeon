from collections import deque
class MyStack(object):

    def __init__(self):
        self.que = deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)

    def pop(self):
        """
        :rtype: int
        """

        n = len(self.que)
        for _ in range(n-1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self):
        """
        :rtype: int
        """
        n = len(self.que)
        for _ in range(n-1):
            self.que.append(self.que.popleft())
        x = self.que.popleft()
        self.que.append(x)
        return x

    def empty(self):
        """
        :rtype: bool
        """
        return not self.que
