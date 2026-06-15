"""
Problem: Design HashMap
Link: https://leetcode.com/problems/design-hashmap/
Pattern: OOD
Difficulty: Medium

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(1) average (O(n/b) with b=1000 buckets), O(n) worst case
Space: O(n + b) = O(n)
"""


class MyHashMap:

    def __init__(self):
        self.SIZE = 1000
        self.buckets = [[] for _ in range(self.SIZE)]
        

    def put(self, key: int, value: int) -> None:
        bucket_index = key % self.SIZE
        bucket = self.buckets[bucket_index]
        exist_index = self._find_index(bucket, key)
        if exist_index == -1:
            bucket.append((key, value))
        else:
            bucket[exist_index] = (key, value)

    def _find_index(self, bucket: list[int], key: int):
        result_index = -1

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                result_index = i
                break
        
        return result_index
            
                        

    def get(self, key: int) -> int:
        bucket_index = key % self.SIZE
        possible_bucket = self.buckets[bucket_index]
        exist_index = self._find_index(possible_bucket, key)
        if exist_index == -1:
            return -1
        else:
            return possible_bucket[exist_index][1]
        

    def remove(self, key: int) -> None:
        bucket_index = key % self.SIZE
        possible_bucket = self.buckets[bucket_index]
        exist_index = self._find_index(possible_bucket, key)
        if exist_index != -1:
            del possible_bucket[exist_index]



        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)


# --- Notes / follow-ups discussed ---
#
