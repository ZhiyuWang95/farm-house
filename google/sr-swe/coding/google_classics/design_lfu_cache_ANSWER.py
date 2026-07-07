"""
Problem: LFU Cache
Link: https://leetcode.com/problems/lfu-cache/
Topic: Design / OOD
Difficulty: Hard

=========================
Explanation
=========================
LFU evicts the entry used fewest times; ties broken by least recently used.
The core challenge: "what is the current minimum frequency?" must be answerable
in O(1), and eviction from that minimum-frequency bucket must also be O(1).

We use three structures:
1. key_map: key → (value, freq) — O(1) lookup and update of value/frequency.
2. freq_map: freq → OrderedDict of keys — each frequency bucket holds its keys
   in insertion order (oldest first), giving O(1) LRU tie-breaking within a bucket.
3. min_freq: integer tracking the current minimum frequency.

On get or put of an existing key: increment its frequency, move it from
freq_map[old_freq] to freq_map[new_freq], update min_freq if the old bucket
is now empty.

On put of a new key: always starts at freq=1, inserted into freq_map[1].
min_freq resets to 1 (a new key is always the least frequent).

On eviction: pop the oldest item from freq_map[min_freq] (the LRU within the
minimum-frequency bucket), delete from key_map.

The OrderedDict per frequency bucket is the same trick as LRU's DLL: O(1)
move_to_end and O(1) popitem(last=False).
=========================
Complexity
=========================
Time:  O(1) for all operations — hashmap lookups and OrderedDict operations
       are all O(1) amortized.
Space: O(capacity) — total entries across all data structures is bounded by
       capacity.
"""

from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_map = {}                              # key -> [val, freq]
        self.freq_map = defaultdict(OrderedDict)       # freq -> {key: None}

    def _increment_freq(self, key: int) -> None:
        val, freq = self.key_map[key]
        del self.freq_map[freq][key]
        if not self.freq_map[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.key_map[key] = [val, freq + 1]
        self.freq_map[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        self._increment_freq(key)
        return self.key_map[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_map:
            self.key_map[key][0] = value
            self._increment_freq(key)
        else:
            if len(self.key_map) == self.capacity:
                evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
                del self.key_map[evict_key]
            self.key_map[key] = [value, 1]
            self.freq_map[1][key] = None
            self.min_freq = 1


if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))    # 1   (freq[1]=2, freq[2]=1)
    cache.put(3, 3)        # evicts key 2 (freq=1, LRU)
    print(cache.get(2))    # -1
    print(cache.get(3))    # 3
    cache.put(4, 4)        # evicts key 1 (freq=2 vs 3's freq=2, but 1 is older... wait)
    print(cache.get(1))    # -1
    print(cache.get(3))    # 3
    print(cache.get(4))    # 4


"""
=========================
Google-asked variations (2-3)
=========================

1. LRU Cache (LeetCode 146, Medium)
   The simpler predecessor — evict by recency only, no frequency tracking.
   Always pair these two in prep: LRU teaches the hashmap+DLL pattern; LFU
   extends it with per-frequency buckets. Interviewers often ask LRU first
   then say "now make it LFU."

2. All O(1) Data Structure (LeetCode 432, Hard)
   "Support insert(key), delete(key), getMaxKey(), getMinKey() all in O(1)."
   Shares the frequency-bucket-as-DLL idea but exposes both min and max ends
   simultaneously. Tests whether you can maintain the full bookkeeping without
   a specific eviction trigger.

3. Design a Log Storage System (LeetCode 635, Medium)
   "Store logs with timestamps; retrieve logs in a time range with a given
   granularity (Year/Month/Day/Hour/Minute/Second)." Not directly LFU, but
   tests the same instinct: multiple hashmaps/buckets indexed by a derived
   key (truncated timestamp), and O(1) insert with range-query retrieval.
   A good "same multi-map pattern, different domain" follow-up.
"""
