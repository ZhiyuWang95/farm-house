"""
Problem: Task Scheduler
Link: https://leetcode.com/problems/task-scheduler/
Topic: Heap
Difficulty: Medium

=========================
Explanation
=========================
Greedy insight: always execute the most frequent remaining task next (to reduce
the chance of forced idle time). A max-heap of (count, task) gives us the most
frequent task in O(log k) where k ≤ 26.

After each interval we either execute a task or idle. When we execute, the task
goes on a cooldown queue with its next-available time. When its cooldown expires,
it returns to the heap.

Algorithm:
1. Count task frequencies, push (-count, task) onto a max-heap.
2. Use a cooldown queue of (next_available_time, -count, task).
3. At each time tick: move tasks from the queue whose cooldown has expired back
   to the heap. If the heap is non-empty, pop the most frequent task, decrement
   its count, push to cooldown if count > 0. If the heap is empty, idle.
4. Repeat until heap and cooldown queue are both empty.

There's also an O(1) math formula: answer = max(total_tasks,
(max_freq - 1) * (n + 1) + count_of_max_freq_tasks). Useful to mention but
the simulation is more general and easier to derive under pressure.
=========================
Complexity
=========================
Time:  O(T log 26) = O(T) where T = len(tasks) — at most T time ticks, each
       heap operation over at most 26 task types.
Space: O(26) = O(1) — heap and queue bounded by number of distinct tasks.
"""

from typing import List
import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # max-heap via negation: most frequent task pops first
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        cooling = deque()  # (ready_at_time, remaining_count)
        time = 0

        while heap or cooling:
            time += 1

            # step 1: if a cooling task is ready, put it back in the heap
            if cooling and cooling[0][0] == time:
                _, count = cooling.popleft()
                heapq.heappush(heap, -count)

            # step 2: run the most frequent available task (or idle if heap empty)
            if heap:
                count = -heapq.heappop(heap)  # undo negation to get actual count
                count -= 1                     # used one occurrence
                if count > 0:                  # still has remaining occurrences
                    cooling.append((time + n + 1, count))

        return time


class Solution2:
    """Math formula — O(n) time, O(1) space, no simulation needed.

    Imagine laying out tasks in a grid where each row has (n+1) slots
    (one execution + n cooldown gaps). The most frequent task drives the
    number of rows:

        [ A _ _ ]   <- row 1:  A + n idle/other slots
        [ A _ _ ]   <- row 2
        [ A B C ]   <- last row: just fill with tasks tied at max_freq

    Total slots = (max_freq - 1) * (n + 1) + count_of_max_freq_tasks

    But if there are enough OTHER tasks to fill every idle slot naturally,
    no idle time is needed and the answer is simply len(tasks).

    So: answer = max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq)
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        count_of_max_freq = sum(1 for f in freq.values() if f == max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq)


if __name__ == "__main__":
    sol = Solution()
    print(sol.leastInterval(["A","A","A","B","B","B"], 2))                           # 8
    print(sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))   # 16
    print(sol.leastInterval(["A","A","A","B","B","B"], 0))                           # 6


"""
=========================
Google-asked variations (2-3)
=========================

1. Reorganize String (LeetCode 767, Medium)
   "Rearrange so no two adjacent characters are the same." Same greedy max-heap
   approach: always place the most frequent remaining character, but alternate
   with the second most frequent when consecutive placement would repeat.
   n=1 special case of Task Scheduler.

2. Rearrange String k Distance Apart (LeetCode 358, Hard)
   "Like Reorganize String but the same character must be at least k positions
   apart." Generalizes Task Scheduler's cooldown to an arbitrary k. Same
   max-heap + cooldown queue, but now k can be larger. Tests whether you can
   parameterize the cooldown.

3. Maximum CPU Load / Scheduling Problems
   A class of Google system-design follow-ups: "given tasks with durations and
   deadlines, schedule to minimize makespan." The heap-based greedy (always pick
   the most urgent/frequent task) is the algorithmic core of real scheduling
   algorithms (EDF, rate-monotonic) — good talking point connecting the coding
   problem to real infra concepts.
"""
