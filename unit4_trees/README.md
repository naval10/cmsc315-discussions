# Unit 4: Employee ID Binary Search Tree

## Completed Implementation

I modeled an employee-ID index using the starter Node and BST classes. The example stored IDs, not full employee records. I completed all 12 TODO blocks and retained the original comments and docstrings.

### Insertion, searching, and traversal

I initialized each node with a value and left and right child references. I used recursive insertion to place smaller IDs on the left and larger IDs on the right. I ignored equal IDs to keep this index unique. I returned updated subtree roots so the first insertion and later child links were retained.

I implemented recursive search with two stopping conditions: a matching node returned True, and a missing node returned False. Each comparison selected one subtree. I implemented in-order traversal by visiting left, current, and right, which returned IDs in sorted order.

### Error handling and testing

I ran the original starter, which printed placeholders, before completing it. I ran the completed program from the Unit 4 folder with:

```bash
python3 unit4_discussion.py
```

On Windows, `py unit4_discussion.py` was an equivalent command when the Python launcher was installed. No third-party packages were required.

| Case tested | Result observed |
| --- | --- |
| Seven IDs spanning both subtrees | In-order traversal matched the sorted IDs. |
| Root, smallest ID, and largest ID | Searches returned True. |
| Missing IDs below and above the stored range | Searches returned False. |
| Empty tree | Traversal returned [] and a valid-ID search returned False. |
| Single node | Height was 1; existing and missing searches worked. |
| Duplicate root and leaf IDs | No extra nodes were added. |
| None, string, float, and Boolean IDs | TypeError was raised before modification. |
| Zero and negative IDs | ValueError was raised before modification. |
| Modification of the traversal result | The tree remained unchanged. |
| Valid insertion after invalid operations | The new ID was found successfully. |
| Balanced, ascending, and descending insertion | Sorted contents matched, but heights differed. |

I required positive integer IDs for this application and rejected Boolean values explicitly because Python treated bool as an int subclass. I caught expected errors in the demonstration so later checks continued. Assertions verified the results when Python ran without optimization. The completed run ended with `All BST checks passed.`

### Insertion order and performance

I inserted [1004, 1002, 1006, 1001, 1003, 1005, 1007] and compared it with the same IDs in ascending and descending order. I measured height in nodes: an empty tree had height 0 and a leaf had height 1.

| Insertion order | Height | Nodes visited for the illustrated search |
| --- | --- | --- |
| Balanced order | 3 | 3 for ID 1007 |
| Ascending order | 7 | 7 for ID 1007 |
| Descending order | 7 | 7 for ID 1001 |

I found that the same sorted traversal did not imply the same tree shape. Search and insertion cost O(h), where h was tree height. A balanced tree had O(log n) height; a chain had O(n) height. Building a tree through sorted insertions could therefore take O(n²) total time. This ordinary BST did not rebalance itself.

Compared with a linear scan of an unsorted list, a balanced BST reduced the search path. I also recognized that a sorted list supported O(log n) binary search, although insertion could require O(n) shifting. A BST was not automatically faster for every operation or workload.

### Memory behavior and growth

I analyzed node storage as O(n) for n unique IDs. Recursive operations used O(h) call-stack space. In-order traversal visited every node in O(n) time and created an O(n) result list in addition to the recursion stack. The height helper also visited all nodes; the iterative search-step helper used O(1) auxiliary space.

I kept the recursive implementation required by the starter. A long skewed tree could exceed Python's recursion limit. For a larger application, I considered an AVL or red-black tree to maintain short paths. Iterative operations could avoid recursion-depth failures but would not by themselves balance the tree.

### Practical application and design reflection

I chose employee IDs because they gave the tree a clear ordering rule and a reason to ignore duplicates. The main implementation decision was to distinguish a valid missing ID from an invalid input: a missing ID returned False, while an invalid input raised a clear exception. I also compared insertion orders rather than assuming sorted output proved efficient searching.

## Submission Status

I completed and locally checked the Python implementation, prepared `discussion_post.md`, and reviewed `submission_checklist.md`. Running the program in IntelliJ, posting the initial discussion, and submitting two peer responses remained unconfirmed.

## Original Assignment Instructions (Retained)

# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
