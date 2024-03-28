class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        name, state, time = logs[0].split(':')
        callstack = [int(name)]
        prevtime = int(time)
        ans = [0 for _ in range(n)]

        for idx in range(1, len(logs)):
            name, state, time = logs[idx].split(':')
            name = int(name)
            time = int(time)
            if state == 'end':
                time += 1
            if callstack:
                currname = callstack[-1]
                ans[currname] += (time-prevtime)
            if state == 'start':
                callstack.append(name)
            else:
                callstack.pop()
            prevtime = time
        

        return ans