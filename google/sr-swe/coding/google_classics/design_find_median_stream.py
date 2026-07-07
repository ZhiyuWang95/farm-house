"""
Problem: Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/
Topic: Design / OOD
Difficulty: Hard

Problem statement:
The median is the middle value in an ordered integer list. If the size of the
list is even, there is no middle value, and the median is the mean of the two
middle values.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data
  structure.
- double findMedian() returns the median of all elements so far. Answers within
  10^-5 of the actual answer will be accepted.

Example:
Input:  ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
        [[],[1],[2],[],[3],[]]
Output: [null,null,null,1.5,null,2.0]

Constraints:
-10^5 <= num <= 10^5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 10^4 calls will be made to addNum and findMedian.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?) per operation
Space: O(?)
"""

import heapq


class MedianFinder:

    def __init__(self):
        self.num_list = []
        

    def addNum(self, num: int) -> None:
        self.num_list.append(num)
        

    def findMedian(self) -> float:
        self.num_list.sort()
        num_count = len(self.num_list)
        if num_count % 2 == 1:
            result = self.num_list[num_count//2]
        else:
            result = (self.num_list[num_count//2] + self.num_list[num_count//2-1])/2
        return result
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
