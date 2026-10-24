# Unit 3: IT Maintenance Task List

## Completed Implementation

I used an editable IT maintenance checklist to demonstrate Python list operations. I completed all seven TODO blocks and retained the starter comments and docstrings. I kept insertion, deletion, and search in separate functions and printed the list after each edit.

### Insertion, deletion, and searching

I implemented `insert_at()` with `list.insert()`. I retained Python's negative-index and endpoint-clamping behavior for integer insertion indices. I rejected noninteger indices, including Boolean values, with TypeError.

I implemented `delete_at()` with index validation followed by `pop()`. I supported valid negative indices and returned None for invalid indices, as required by the starter. I checked the index before modifying the list.

I implemented `search_value()` as a sequential scan using `enumerate()`. I returned the first matching index or -1 when no match was found. I handled -1 as a missing-value signal instead of using it to index the list.

### Error handling and testing

I ran the original starter, which printed placeholders. After completing it, I ran the program from the Unit 3 folder:

```bash
python3 unit3_discussion.py
```

On Windows, `py unit3_discussion.py` was an equivalent command when the Python launcher was installed. The program required no third-party packages.

| Case tested | Result observed |
| --- | --- |
| Beginning, middle, and end insertion | Tasks appeared in the expected positions. |
| Beginning, middle, and end deletion | The correct task was returned and remaining tasks stayed ordered. |
| Existing and missing values | Search returned the matching index or -1. |
| Empty insertion | The new task became the only item. |
| Empty deletion and search | Results were None and -1 respectively. |
| Single-item deletion | The list became empty. |
| Out-of-range and noninteger deletion indices | None was returned and the list stayed unchanged. |
| Valid negative deletion indices | The last and first items were removed correctly. |
| Extreme integer insertion indices | Python clamped insertion to the beginning or end. |
| Noninteger insertion indices | TypeError was caught without changing the list. |
| Duplicate values | Search returned the first matching index. |
| None, zero, and empty-string values | The generic helpers accepted these stored values. |
| Valid operation after invalid requests | A later task was added and found successfully. |

The completed run printed `All list checks passed.` Assertions checked the observed results when Python ran without optimization.

### Design decisions and limitations

I allowed arbitrary stored values because the starter functions were general list helpers. The maintenance demonstration used strings. A full task-management application could separately reject blank descriptions and assign unique task IDs.

I followed the required None return value for invalid deletion. This result was ambiguous if a valid stored None was removed, so I tested both the return value and the resulting contents. For a different API, I would consider an exception or a separate success flag to distinguish these outcomes.

### Performance and memory behavior

I analyzed Python lists as dynamic arrays of object references. Index access took O(1). Beginning and middle insertions or deletions could shift O(n) references. Insertion at the end had amortized O(1) cost, with occasional O(n) resizing. Removing the last element also had amortized O(1) cost. Linear search required up to O(n) equality comparisons; comparison cost could also depend on the stored values.

I analyzed list storage as O(n) references, plus the memory of the stored objects and spare allocated capacity. A linked list also used O(n) storage but required links and node overhead.

I concluded that a linked list could outperform an array-based list for frequent insertions after a known node, or deletions when the required node and predecessor references were already available. A doubly linked list could delete a known node in O(1). Finding a node by position or value could still take O(n), so linked lists were not automatically faster for all edits. Python lists offered direct indexing and generally better locality for their reference arrays.

### Practical application and design reflection

I chose maintenance tasks because their order could change as priorities changed. I added an urgent task first, inserted a scan in the middle, and appended documentation at the end. I kept the Python list because the checklist was small and easy to index and display. For a much larger workload, I would choose a structure based on whether indexed access, end operations, or edits at already-known nodes were most common.

## Submission Status

I completed and locally checked the code, prepared `discussion_post.md`, and reviewed `submission_checklist.md`. Running the program in IntelliJ and posting the initial discussion and two peer responses remained unconfirmed.

## Original Assignment Instructions (Retained)

# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

