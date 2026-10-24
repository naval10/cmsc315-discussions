# Initial Discussion Post Draft

GitHub repository: https://github.com/naval10/cmsc315-discussions

## Design Approach

I modeled an employee-ID index with Node and BST classes. I used recursive insertion and search, placed smaller IDs on the left and larger IDs on the right, and ignored duplicates. In-order traversal returned the IDs in sorted order.

## Reflection

This assignment helped me understand why insertion order matters as much as the values stored in a BST. I inserted the same seven employee IDs in balanced, ascending, and descending orders. The balanced order produced a height of three nodes, while both sorted orders produced a height of seven. Searching for ID 1007 visited three nodes in the balanced tree and seven in the ascending tree.

One challenge was separating valid missing IDs from invalid inputs. I returned False for a missing positive integer ID but raised clear exceptions for invalid types or nonpositive values. I also checked empty trees, single nodes, duplicates, and whether modifying the traversal result changed the tree.

A balanced BST can search in O(log n) time because comparisons eliminate subtrees, improving on an unsorted list's O(n) linear search. However, sequential insertions can create a chain and reduce search performance to O(n). A sorted list also supports fast binary search, so the best choice depends on the operations needed. For a larger employee index, I would consider a self-balancing tree to keep search paths short.

## Memory and Reliability

The tree used O(n) node storage and O(h) recursion space, where h represented its height. The sorted traversal also created an O(n) output list. A long skewed tree could reach Python's recursion limit; this implementation did not rebalance automatically.

How did insertion order affect your tree, and how did you handle duplicate values?
