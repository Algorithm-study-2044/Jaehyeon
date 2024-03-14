import random
class RandomizedSet(object):

    def __init__(self):
        self.S = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.S:
            return False
        else:
            self.S.add(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.S:
            self.S.discard(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        random_el = random.sample(self.S, 1)[0]
        return random_el

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()