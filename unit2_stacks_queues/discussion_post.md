# Initial Discussion Post Draft

GitHub repository: https://github.com/naval10/cmsc315-discussions

## Design Approach

I used a text-editor undo history for my stack and a support-desk ticket line for my queue. I implemented the stack with a Python list and the queue with `collections.deque`. Each class kept its operations in separate methods. I preserved the TODO prompts and added comments explaining the order of removal and how previews worked.

## Reflection

This assignment helped me understand how the location of additions and removals determines a data structure's behavior. A stack uses last-in, first-out (LIFO) because values enter and leave at the same end, called the top. In my text-editor example, the most recent action was undone first. A queue uses first-in, first-out (FIFO) because values enter at the back and leave from the front. My support-desk example processed the oldest ticket first.

One challenge was deciding what an empty operation should return. Returning None could be confusing because None was also a valid stored value. I addressed this by raising clear IndexError exceptions for empty removals and previews. The demonstration caught those exceptions and continued.

I tested empty structures, single items, repeated values, and interleaved additions and removals. I also checked that previewing did not remove an item. These checks helped me connect the expected behavior to the actual output. I learned that choosing the right structure involves both ordering requirements and decisions about how invalid operations should be handled.

## Memory and Reliability

Each structure used O(n) storage for n item references, with additional memory for the objects themselves. Adding more items increased memory use. I used deque.popleft() to avoid shifting queue elements during removal. For a larger application, I would consider a capacity limit and a clear response when the queue became full.

How did you handle empty operations in your implementation, and would you add a capacity limit?
