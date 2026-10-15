# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Completed implementation

I implemented Stack with a Python list and Queue with collections.deque. I kept every TODO prompt and added comments explaining LIFO, FIFO, and non-removing previews. I moved the demonstration code inside main so importing the classes did not run the examples.

I used a text-editor undo history for the stack and a support-desk ticket line for the queue. Each demonstration added four values, previewed the next value, and removed all values in the expected order.

### Design decisions

I used append and pop at the end of the list for stack operations. I used append and popleft on the deque for queue operations, which avoided shifting remaining elements as list.pop(0) would have done.

I raised IndexError with a descriptive message when a removal or preview was attempted on an empty structure. The demonstration caught these expected exceptions and continued. I allowed arbitrary stored values, including None, zero, and empty strings; those values were valid data rather than signals for an empty structure. I did not impose a fixed capacity.

### Verification

I ran the starter before editing; it printed instructions but did not implement the operations. After completing it, I ran:

```bash
python3 unit2_stacks_queues/unit2_discussion.py
```

I verified the following with assertions:
- Stack removals followed reverse insertion order.
- Queue removals followed insertion order.
- Preview operations left the next value available for removal.
- Empty removals and previews raised IndexError.
- Single-item structures became empty after removal.
- Duplicate values and falsy values were preserved.
- Interleaved additions and removals preserved the correct order.

The completed run ended with:
```text
All ordering, preview, empty, single-item, and extra assertions passed.
```

### Efficiency and memory

I used operations with O(1) deque endpoint costs and amortized O(1) list append and end-pop costs. Preview and empty checks took O(1). I analyzed container storage as O(n) for n references, with additional memory for the stored objects. I recognized that these dynamically growing structures were still limited by available memory.

### Checklist review

I completed the code, comments, custom scenarios, additional tests, edge cases, and README documentation. I retained the original TODO prompts. Running the program in IntelliJ and posting the discussion and two peer responses remained user-side steps.

## Completed discussion reflection

GitHub repository: https://github.com/naval10/cmsc315-discussions

For this assignment, I implemented a stack with a Python list and a queue with collections.deque. I used text-editor actions to demonstrate undo behavior and support tickets to demonstrate requests being processed in arrival order. Keeping each operation in its own method made the code easier to follow and test.

A stack uses last-in, first-out (LIFO) because items are added and removed at the same end, called the top. The most recent edit is therefore undone first. A queue uses first-in, first-out (FIFO) because items enter at the back and leave from the front. This fits a support desk that handles tickets in arrival order.

One challenge was distinguishing an empty structure from a valid stored value such as None. I handled invalid removals and previews with clear IndexError messages. I also tested empty structures, single items, repeated values, and interleaved operations.

Both structures use O(n) storage for n item references. Adding more items increases memory use, and longer stored descriptions require additional space. This assignment helped me connect predictable ordering with practical application design.

