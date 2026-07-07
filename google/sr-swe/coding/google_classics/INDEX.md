# Google Classics — Algorithm Topic Reference Library

Not date-based like `coding/solutions/` — this is a standing reference library
organized by algorithm topic, covering the patterns most frequently asked in
Google interviews. Each question has two files:

- `<topic>_<question>.py` — problem statement + signature stub, no spoilers. Use this to self-test blind.
- `<topic>_<question>_ANSWER.py` — full solution, detailed explanation, and 2-3 Google-asked variations on the same pattern.

## Recursion

- [x] [Pow(x, n)](https://leetcode.com/problems/powx-n/) (Medium) — `recursion_pow_x_n.py`
- [x] [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (Medium) — `recursion_generate_parentheses.py`

## Linked List

- [x] [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy) — `linkedlist_merge_two_sorted_lists.py`
- [ ] [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium) — `linkedlist_cycle_ii.py`

## BFS

- [x] [Rotting -](https://leetcode.com/problems/rotting-oranges/) (Medium) — `bfs_rotting_oranges.py`
- [x] [Word Ladder](https://leetcode.com/problems/word-ladder/) (Hard) — `bfs_word_ladder.py`

## DFS (top-3 popularity topic — 2 extra questions added)

- [x] [Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium) — `dfs_number_of_islands.py`
- [ ] [Word Search](https://leetcode.com/problems/word-search/) (Medium) — `dfs_word_search.py`
- [ ] [Permutations](https://leetcode.com/problems/permutations/) (Medium) — `dfs_permutations.py`
- [x] [Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium) — `dfs_combination_sum.py`

### DFS Variations

- [ ] [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) (Medium) — `dfs_max_area_island.py`
- [ ] [Word Search II](https://leetcode.com/problems/word-search-ii/) (Hard) — `dfs_word_search_ii.py`
- [ ] [N-Queens](https://leetcode.com/problems/n-queens/) (Hard) — `dfs_n_queens.py`
- [ ] [Permutations II](https://leetcode.com/problems/permutations-ii/) (Medium) — `dfs_permutations_ii.py`
- [ ] [Next Permutation](https://leetcode.com/problems/next-permutation/) (Medium) — `dfs_next_permutation.py`
- [ ] [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) (Medium) — `dfs_combination_sum_ii.py`
- [ ] [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) (Medium) — `dfs_combination_sum_iii.py`
- [ ] [Path with Maximum Gold](https://leetcode.com/problems/path-with-maximum-gold/) (Medium) — `dfs_path_max_gold.py`

## Tree (top-3 popularity topic — 2 extra questions added)

- [x] [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) (Medium) — `tree_lowest_common_ancestor.py`
- [ ] [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) (Hard) — `tree_serialize_deserialize.py`
- [x] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (Medium) — `tree_validate_bst.py`
- [ ] [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (Hard) — `tree_max_path_sum.py`

### Tree Variations

- [ ] [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) (Medium) — `tree_lca_bst.py`
- [ ] [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (Medium) — `tree_kth_smallest_bst.py`
- [ ] [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) (Medium) — `tree_recover_bst.py`
- [ ] [Convert Sorted Array to BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) (Easy) — `tree_sorted_array_to_bst.py`
- [ ] [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) (Easy) — `tree_diameter.py`
- [ ] [House Robber III](https://leetcode.com/problems/house-robber-iii/) (Medium) — `tree_house_robber_iii.py`
- [ ] [Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/) (Medium) — `tree_serialize_bst.py`
- [ ] [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Medium) — `tree_encode_decode_strings.py`

## Graph (top-3 popularity topic — 2 extra questions added)

- [x] [Course Schedule](https://leetcode.com/problems/course-schedule/) (Medium) — `graph_course_schedule.py`
- [ ] [Clone Graph](https://leetcode.com/problems/clone-graph/) (Medium) — `graph_clone_graph.py`
- [ ] [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) (Medium) — `graph_pacific_atlantic.py`
- [ ] [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Medium) — `graph_network_delay_time.py`

### Graph Variations

- [ ] [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (Medium) — `graph_course_schedule_ii.py`
- [ ] [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) (Hard) — `graph_alien_dictionary.py`
- [ ] [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) (Medium) — `graph_minimum_height_trees.py`
- [ ] [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (Medium) — `graph_cheapest_flights.py`
- [ ] [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) (Medium) — `graph_max_probability.py`
- [ ] [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (Medium) — `graph_surrounded_regions.py`
- [ ] [Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/) (Medium) — `graph_number_of_enclaves.py`
- [ ] [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) (Hard) — `graph_trapping_rain_water_ii.py`

## DP (top-5 popularity topic)

- [ ] [Coin Change](https://leetcode.com/problems/coin-change/) (Medium) — `dp_coin_change.py`
- [ ] [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) (Medium) — `dp_longest_increasing_subsequence.py`
- [ ] [Word Break](https://leetcode.com/problems/word-break/) (Medium) — `dp_word_break.py`
- [ ] [Unique Paths](https://leetcode.com/problems/unique-paths/) (Medium) — `dp_unique_paths.py`
- [ ] [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) (Medium) — `dp_longest_common_subsequence.py`
- [ ] [House Robber](https://leetcode.com/problems/house-robber/) (Medium) — `dp_house_robber.py`

### DP Variations

- [ ] [House Robber II](https://leetcode.com/problems/house-robber-ii/) (Medium) — `dp_house_robber_ii.py`
- [ ] [Decode Ways](https://leetcode.com/problems/decode-ways/) (Medium) — `dp_decode_ways.py`
- [ ] [Jump Game](https://leetcode.com/problems/jump-game/) (Medium) — `dp_jump_game.py`
- [ ] [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) (Medium) — `dp_partition_equal_subset.py`

## Heap (top-5 popularity topic)

- [x] [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium) — `heap_kth_largest.py`
- [x] [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium) — `heap_top_k_frequent.py`
- [x] [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (Hard) — `heap_find_median_stream.py`
- [x] [Task Scheduler](https://leetcode.com/problems/task-scheduler/) (Medium) — `heap_task_scheduler.py`

### Heap Variations

- [ ] [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (Medium) — `heap_k_closest_points.py`
- [ ] [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) — `heap_merge_k_sorted_lists.py`
- [ ] [Reorganize String](https://leetcode.com/problems/reorganize-string/) (Medium) — `heap_reorganize_string.py`

## Sliding Window (top-5 popularity topic)

- [ ] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium) — `sliding_window_longest_substring.py`
- [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard) — `sliding_window_minimum_window.py`
- [ ] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Hard) — `sliding_window_maximum.py`
- [ ] [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (Medium) — `sliding_window_char_replacement.py`

## Design / OOD (high priority for Sr SWE)

- [x] [LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium) — `design_lru_cache.py`
- [ ] [LFU Cache](https://leetcode.com/problems/lfu-cache/) (Hard) — `design_lfu_cache.py`
- [ ] [Design Twitter](https://leetcode.com/problems/design-twitter/) (Medium) — `design_twitter.py`
- [ ] [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) (Medium) — `design_insert_delete_getrandom.py`
- [x] [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (Hard) — `design_find_median_stream.py`

---

Check items off here as you work through them blind, independent of `coding/problem_list.md`'s daily cadence.