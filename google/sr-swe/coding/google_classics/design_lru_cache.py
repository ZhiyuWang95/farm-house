"""
Problem: LRU Cache
Link: https://leetcode.com/problems/lru-cache/
Topic: Design / OOD
Difficulty: Medium

Problem statement:
Design a data structure that follows the constraints of a Least Recently
Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise
  return -1.
- void put(int key, int value) Update the value of the key if the key exists.
  Otherwise, add the key-value pair to the cache. If the number of keys
  exceeds the capacity from this operation, evict the least recently used key.

Both get and put must run in O(1) average time complexity.

Example:
Input:  ["LRUCache","put","put","get","put","get","put","get","get","get"]
        [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
Output: [null,null,null,1,null,-1,null,-1,3,4]

Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?) per operation
Space: O(?)
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, targetNode):
        targetNode.prev.next = targetNode.next
        targetNode.next.prev = targetNode.prev

    def _add_front(self, targetNode):
        targetNode.next = self.head.next
        targetNode.prev = self.head
        self.head.next.prev = targetNode
        self.head.next = targetNode


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        resultNode = self.cache[key]
        self._remove(resultNode)
        self._add_front(resultNode)
        return resultNode.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            existNode = self.cache[key]
            self._remove(existNode)
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self._add_front(newNode)

        if len(self.cache) > self.cap:
            last_node = self.tail.prev
            self._remove(last_node)
            del self.cache[last_node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
