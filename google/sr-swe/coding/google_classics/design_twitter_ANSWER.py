"""
Problem: Design Twitter
Link: https://leetcode.com/problems/design-twitter/
Topic: Design / OOD
Difficulty: Medium

=========================
Explanation
=========================
Each user has a list of their own tweets (stored newest-first) and a set of
followees. getNewsFeed must merge the tweet streams of all followees (plus the
user themselves) and return the 10 most recent globally.

The merge is a classic k-way merge using a max-heap. Each followee contributes
their tweet list; we use a global timestamp counter (decremented so that larger
timestamp = more recent) to compare tweets across users. We push the most recent
tweet from each followee onto the heap, then pop-and-advance 10 times.

A global integer timestamp (not real time) gives total ordering across all
postTweet calls. Storing it as negative in the heap makes Python's min-heap
behave as a max-heap (most recent tweet pops first).

Key insight: you don't need to sort all tweets at feed-generation time. The heap
only ever holds at most one tweet per followee, so heap size is bounded by the
number of followees, not total tweet count.
=========================
Complexity
=========================
Time:  postTweet O(1), follow/unfollow O(1), getNewsFeed O(F log F + 10 log F)
       where F = number of followees — heap of size F, 10 pops each with log F
       reheap.
Space: O(U + T) where U = users, T = total tweets stored.
"""

from typing import List
from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)    # userId -> [(neg_time, tweetId), ...]
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followees = self.following[userId] | {userId}
        for uid in followees:
            if self.tweets[uid]:
                neg_time, tid = self.tweets[uid][-1]
                # (neg_time, tweetId, userId, index into that user's tweet list)
                heapq.heappush(heap, (neg_time, tid, uid, len(self.tweets[uid]) - 1))

        feed = []
        while heap and len(feed) < 10:
            neg_time, tid, uid, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:
                neg_time2, tid2 = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (neg_time2, tid2, uid, idx - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


if __name__ == "__main__":
    t = Twitter()
    t.postTweet(1, 5)
    print(t.getNewsFeed(1))   # [5]
    t.follow(1, 2)
    t.postTweet(2, 6)
    print(t.getNewsFeed(1))   # [6, 5]
    t.unfollow(1, 2)
    print(t.getNewsFeed(1))   # [5]


"""
=========================
Google-asked variations (2-3)
=========================

1. Merge K Sorted Lists (LeetCode 23, Hard)
   The getNewsFeed k-way merge is exactly this problem. Each followee's tweet
   list is one sorted list; you need the top 10 elements globally. Understanding
   Merge K Sorted Lists first makes the heap pattern in Design Twitter obvious.

2. Design Twitter with pagination
   "getNewsFeed(userId, page, pageSize) — support paginated feed retrieval."
   The heap approach naturally extends: keep a cursor per user (the index you
   stopped at), store the heap state between calls. Tests whether you can make
   a stateful iterator out of the merge logic.

3. Twitter with trending topics
   "Add a getTrending() method returning the top 10 most-tweeted hashtags in
   the last hour." Introduces a sliding window + heap or bucket-count on top of
   the existing structure — a common "extend your design" follow-up that tests
   whether your architecture is extensible.
"""
