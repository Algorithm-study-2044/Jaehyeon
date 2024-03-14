class Node:
    def __init__(self, key, value, prevNode, nextNode):
        self.key = key
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cachedict = dict()
        self.headNode = Node(None, None, None, None)
        self.tailNode = Node(None, None, None, None)
        self.headNode.nextNode = self.tailNode
        self.tailNode.prevNode = self.headNode

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cachedict.keys():
            ansNode = self.cachedict[key]
            # delete ansNode
            ansNode.prevNode.nextNode = ansNode.nextNode
            ansNode.nextNode.prevNode = ansNode.prevNode
            # push at head
            ansNode.prevNode = self.headNode
            ansNode.nextNode = self.headNode.nextNode
            ansNode.prevNode.nextNode = ansNode
            ansNode.nextNode.prevNode = ansNode
            return ansNode.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cachedict.keys():
            targetNode = self.cachedict[key]
            targetNode.value = value
            # delete targetNode
            targetNode.prevNode.nextNode = targetNode.nextNode
            targetNode.nextNode.prevNode = targetNode.prevNode
            # push targetNode at head
            targetNode.prevNode = self.headNode
            targetNode.nextNode = self.headNode.nextNode
            targetNode.prevNode.nextNode = targetNode
            targetNode.nextNode.prevNode = targetNode
        else:
            targetNode = Node(key, value, self.headNode, self.headNode.nextNode)
            # push targetNode at head
            targetNode.prevNode.nextNode = targetNode
            targetNode.nextNode.prevNode = targetNode
            # add to dict
            self.cachedict[key] = targetNode
            
            if len(self.cachedict)>self.capacity:
                # delete endNode
                deleteNode = self.tailNode.prevNode
                deleteNode.prevNode.nextNode = deleteNode.nextNode
                deleteNode.nextNode.prevNode = deleteNode.prevNode
                del self.cachedict[deleteNode.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)