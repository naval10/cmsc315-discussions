# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.


## Completed Implementation

I completed all five student TODO blocks and retained the original prompts and comments. I implemented both algorithms directly rather than calling Python's built-in search helpers. I used an IT asset intake scenario: I searched arrival-order IDs linearly and created an ascending copy for binary search. I preserved the original list and checked that indices referred to their respective lists.

### Running the program

From the repository root:

```bash
python unit5_searching_analysis/unit5_discussion.py
```

I ran the original starter first; it printed three placeholder sections. After implementation, I ran the updated script with assertions enabled and received:

```text
All small, large, edge-case, and asset lookup assertions passed.
```

### Design and complexity

I made linear search return the first matching index, or -1 after exhausting the list. I made iterative binary search return a matching index, or -1 when its inclusive bounds crossed. For duplicates, I allowed binary search to return any matching index, as the starter did not require the first occurrence.

| Operation | Best case | Worst case | Auxiliary space |
| --- | --- | --- | --- |
| Linear search | O(1) | O(n) | O(1) |
| Iterative binary search on a sorted Python list | O(1) | O(log n) | O(1) |
| Creating the sorted copy | O(n) for already ordered input | O(n log n) | O(n) |

I kept sorting outside binary_search. I treated ascending order and comparable values as preconditions, because checking the entire list on every call would add O(n) work. I did not support None as a list or mixed, noncomparable values. Empty lists were valid and returned -1. Unsorted data violated the binary-search contract and could produce an incorrect result, so I used linear search or sorted a copy first. I used lists because midpoint indexing was constant-time; linked lists would not provide the same access advantage.

### Tests and observed results

I verified five-item and 100,000-item sorted datasets. I checked present and absent targets, empty and single-item lists, both endpoints, targets outside the range, an internal gap, negative values and zero, duplicates, and sorted strings. I also asserted that the asset scenario left the arrival-order list unchanged.

I averaged 100 searches per algorithm and target on the large dataset. One local run produced these results; times were machine-dependent and were not pass/fail thresholds.

| Target in 100,000 items | Linear average in microseconds | Binary average in microseconds | Returned index |
| --- | --- | --- | --- |
| 99,999 | 2956.24 | 1.34 | 99,999 |
| 100,000, absent | 3197.89 | 1.35 | -1 |

I selected a last-item and a missing target to demonstrate worst-case linear scans. Each required 100,000 linear visits, while binary search required at most 17 midpoint visits. I did not count sorting or dataset construction in these timings. I recognized that a first-item lookup could favor linear search, and that small timing differences could reflect overhead or system load.

### Preparation and practical use

I used linear search for a one-time lookup in unsorted incoming equipment. Sorting solely for that lookup would cost more asymptotic work than scanning once. I used a reusable sorted copy for repeated asset-ID queries. I noted that updates could require rebuilding or maintaining that order, and that the copy consumed O(n) additional storage. Both search loops themselves used constant extra space.

## Completed Reflection

I implemented linear and binary search using an IT asset lookup scenario. Linear search checked asset IDs in arrival order, while binary search used a sorted copy for repeated lookups. This helped me understand that choosing an algorithm depended on how the data was organized and how often it would be searched.

The main challenge was keeping the binary search boundaries correct. I used low and high indices and moved each boundary past the midpoint after an unsuccessful comparison. I tested empty lists, single items, missing values, first and last positions, and duplicates. I also checked that both searches located the same asset even when its index changed after sorting.

The larger dataset showed why halving the remaining candidates reduced search work. However, I excluded sorting from the timed searches, so the measurements represented lookup time rather than total preparation cost. For a one-time check of an unsorted intake list, I would choose linear search. For repeated searches of stable, sorted IDs, I would choose binary search. I learned that faster lookups could justify preparation, but sorting was not automatically worthwhile for every task.
