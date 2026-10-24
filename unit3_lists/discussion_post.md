# Initial Discussion Post Draft

GitHub repository: https://github.com/naval10/cmsc315-discussions

## Design Approach

I used an IT maintenance checklist to demonstrate list operations. My program added tasks at the beginning, middle, and end, removed tasks from those positions, and searched for existing and missing tasks. Separate helper functions kept each operation easy to follow.

## Reflection

This assignment helped me understand how list operations affect both ordering and performance. Adding an urgent task at the beginning moved the existing references to later positions. Appending a task at the end usually avoided that shifting. My example showed how a support team could organize tasks such as checking backups, scanning devices, and reviewing logs.

One challenge was handling invalid indices without changing the list. I validated deletion indices and returned None when they were invalid, as the starter required. I also tested empty lists, single items, negative indices, duplicates, and missing values. Search returned the first matching index or -1 when no match existed.

A linked list might outperform an array-based list when insertions or deletions occur frequently and the required node references are already known. Those edits can avoid shifting later elements. However, locating a node can still take O(n), and linked lists require extra link storage. Python lists provide O(1) indexed access, while beginning and middle edits can take O(n). For my small maintenance checklist, a Python list offered a practical balance of readable code and convenient access.

## Memory and Reliability

The list used O(n) references plus storage for its values. Returning None for invalid deletion was ambiguous when the removed value itself was None, so I checked the resulting list in that test. A larger application could use a separate success flag or an exception.

Which operations were most common in your scenario, and how did they influence your choice of list?
