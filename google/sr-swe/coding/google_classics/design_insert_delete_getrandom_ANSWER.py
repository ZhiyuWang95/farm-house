"""
Problem: Insert Delete GetRandom O(1)
Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
Topic: Design / OOD
Difficulty: Medium

=========================
Explanation
=========================
getRandom requires uniform random access, which means we need an array (so we
can index into it with random.randint). But plain arrays have O(n) delete.

The trick: keep a dynamic array of values AND a hashmap from value to its index
in the array. Insert appends to the array and records the index. For delete, we
can't just remove from the middle (that's O(n) shift). Instead, swap the target
element with the last element, update the last element's index in the hashmap,
then pop from the end — all O(1). getRandom just picks a random index.

The swap-with-last trick is the key insight. It works because we don't care
about order — only that every element is reachable by a valid index.

Watch out: when deleting the last element, the swap is a no-op (swapping with
itself), but you still need to delete the hashmap entry for the removed value
before the pop — otherwise you'd overwrite the wrong index if the value you're
deleting happens to be the last element.
=========================
Complexity
=========================
Time:  O(1) average for all three operations — array append/pop is amortized
       O(1), hashmap operations are O(1) average.
Space: O(n) where n is the number of elements currently in the set.
"""

import random


class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}   # value -> index in array
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last = self.arr[-1]
        self.arr[idx] = last
        self.val_to_idx[last] = idx
        self.arr.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


if __name__ == "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))    # True
    print(rs.remove(2))    # False
    print(rs.insert(2))    # True
    print(rs.getRandom())  # 1 or 2
    print(rs.remove(1))    # True
    print(rs.insert(2))    # False
    print(rs.getRandom())  # 2


"""
=========================
Google-asked variations (2-3)
=========================

1. Insert Delete GetRandom O(1) - Duplicates Allowed (LeetCode 381, Hard)
   "Allow duplicate values; getRandom should return each occurrence with equal
   probability." Change val_to_idx to val_to_set_of_indices (each value maps to
   a set of indices it occupies). The swap trick still works but now you pick any
   index from the set for the value being deleted. Tests whether you can handle
   the multi-index bookkeeping on top of the same core pattern.

2. Shuffle an Array (LeetCode 384, Medium)
   "Implement reset() (restore original) and shuffle() (uniform random
   permutation)." The Fisher-Yates shuffle is the in-place O(n) algorithm for
   this — swap each element with a random element from the remaining unshuffled
   portion. The swap-with-last deletion above is essentially one step of
   Fisher-Yates, so these problems share the same underlying intuition.

3. Design Skiplist (LeetCode 1206, Hard)
   "Implement a skiplist supporting search, add, erase in O(log n) average."
   Not O(1), but a common "can you design a probabilistic data structure from
   scratch?" follow-up. Tests a different dimension: pointer-based structure
   building, similar to the DLL in LRU Cache but with probabilistic height.
"""
