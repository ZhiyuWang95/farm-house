"""
Problem: Design HashSet
Link: https://leetcode.com/problems/design-hashset/
Pattern: OOD
Difficulty: Easy

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(1) average (O(n/b) with b=1000 buckets), O(n) worst case
Space: O(n + b) = O(n)
"""


class MyHashSet:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = [[] for _ in range(self.bucket_size)]

    def add(self, key: int) -> None:
        bucket_index = key % self.bucket_size
        current_bucket = self.buckets[bucket_index]
        if key not in current_bucket:
            current_bucket.append(key)
        return
        

    def remove(self, key: int) -> None:
        bucket_index = key % self.bucket_size
        current_bucket = self.buckets[bucket_index]
        if key in current_bucket:
            current_bucket.remove(key)
        return
        

    def contains(self, key: int) -> bool:
        bucket_index = key % self.bucket_size
        current_bucket = self.buckets[bucket_index]
        return key in current_bucket
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# --- Notes / follow-ups discussed ---
#
# Your object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
