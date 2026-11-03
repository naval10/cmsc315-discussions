# Unit 5 Discussion Post

Repository: https://github.com/naval10/cmsc315-discussions
Week 5 files: https://github.com/naval10/cmsc315-discussions/tree/master/unit5_searching_analysis

## Design and Search Analysis

I used an IT asset lookup scenario to compare linear and binary search. My program searched an unsorted list of arriving asset IDs with linear search, then searched a sorted copy with binary search. I kept the original arrival order intact and showed that the same asset had different indices in the two lists.

Binary search reduced the remaining candidates by half after each unsuccessful comparison. On a sorted Python list, that gave it O(log n) worst-case search time, compared with O(n) for linear search. With 100,000 items, binary search needed at most 17 midpoint visits, while a missing target required linear search to inspect every item. Both algorithms could succeed in O(1) time when their first examined item matched.

Linear search remained appropriate for a one-time search of an unsorted equipment intake list. Sorting first would add preparation work that a single lookup might not justify. Binary search could not reliably search arbitrary unsorted data or values without a consistent ordering rule. It also could not use this indexed implementation on a stream without first storing the data. A linked list lacked the constant-time midpoint access needed for the same time bound.

I tested empty lists, single items, missing values, endpoints, duplicates, and sorted strings. All assertions passed. The large-data timing comparison excluded sorting and dataset creation, so I treated it as a comparison of lookup costs, not total application costs.

## Reflection

I implemented linear and binary search using an IT asset lookup scenario. Linear search checked asset IDs in arrival order, while binary search used a sorted copy for repeated lookups. This helped me understand that choosing an algorithm depended on how the data was organized and how often it would be searched.

The main challenge was keeping the binary search boundaries correct. I used low and high indices and moved each boundary past the midpoint after an unsuccessful comparison. I tested empty lists, single items, missing values, first and last positions, and duplicates. I also checked that both searches located the same asset even when its index changed after sorting.

The larger dataset showed why halving the remaining candidates reduced search work. However, I excluded sorting from the timed searches, so the measurements represented lookup time rather than total preparation cost. For a one-time check of an unsorted intake list, I would choose linear search. For repeated searches of stable, sorted IDs, I would choose binary search. I learned that faster lookups could justify preparation, but sorting was not automatically worthwhile for every task.
