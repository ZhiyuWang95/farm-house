"""
Problem: Design Twitter
Link: https://leetcode.com/problems/design-twitter/
Topic: Design / OOD
Difficulty: Medium

Problem statement:
Design a simplified version of Twitter where users can post tweets, follow/unfollow
another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId
  by the user userId. Each call to this function will be made with a unique tweetId.
- List[int] getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the
  user's news feed. Each item in the news feed must be posted by users who the user
  followed or by the user themselves. Tweets must be ordered from most recent to least
  recent.
- void follow(int followerId, int followeeId) The user with ID followerId starts
  following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId starts
  unfollowing the user with ID followeeId.

Example:
Input:  ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed",
          "unfollow","getNewsFeed"]
        [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
Output: [null,null,[5],null,null,[6,5],null,[5]]

Constraints:
1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 10^4
All the tweets have unique IDs.
At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?) per operation
Space: O(?)
"""

from typing import List
from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass
