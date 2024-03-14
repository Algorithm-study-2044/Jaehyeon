class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        inputdict = dict()
        for transaction in transactions:
            a, b, c, d = transaction.split(',')
            if a in inputdict.keys():
                inputdict[a].append((int(b),int(c),d))
            else:
                inputdict[a] = [(int(b),int(c),d)]
        
        ans = set()
        for name in inputdict.keys():
            transes = inputdict[name]
            transes = sorted(transes, key=lambda x: x[0])
            for idx, (b,c,d) in enumerate(transes):
                for idx_ in range(idx+1, len(transes)):
                    b_, c_, d_ = transes[idx_]
                    if b_>b+60:
                        break
                    else:
                        if d != d_:
                            ans.add((name+','+str(b)+','+str(c)+','+d, idx))
                            ans.add((name+','+str(b_)+','+str(c_)+','+d_, idx_))
            for idx, (b,c,d) in enumerate(transes):
                if c>1000:
                    ans.add((name+','+str(b)+','+str(c)+','+d, idx))
            
        realans = []
        for s, i in ans:
            realans.append(s)
        return realans