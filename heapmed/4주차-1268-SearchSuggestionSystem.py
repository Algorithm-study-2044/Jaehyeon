class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        startidx = 0
        ans = []
        for wordidx in range(len(searchWord)):
            arr = []
            while startidx < len(products) and products[startidx] < searchWord[:wordidx+1]:
                startidx += 1
            for idx in range(startidx, min(startidx+3, len(products))):
                if products[idx].startswith(searchWord[:wordidx+1]):
                    arr.append(products[idx])
            ans.append(arr)
        return ans