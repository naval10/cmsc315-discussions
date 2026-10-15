# Unit 2: Text Editor Undo and Support Desk Queue

## Completed Implementation

I implemented `Stack` with a Python list and `Queue` with `collections.deque`. I retained all 12 original TODO prompts and added comments explaining LIFO, FIFO, and non-removing previews. I placed the demonstrations inside `main()` so importing the classes did not run the examples.

### Stack and queue operations

- I implemented `push()`, `pop()`, `peek()`, and `is_empty()` for the stack.
- I implemented `enqueue()`, `dequeue()`, `front()`, and `is_empty()` for the queue.
- I added and removed stack values at the same end to demonstrate LIFO.
- I added queue values at the back and removed them from the front to demonstrate FIFO.
- I used `peek()` and `front()` to preview values without removing them.

### Error handling and testing

I ran the starter, which printed placeholders, and then ran the completed program from the Unit 2 folder with:

```bash
python3 unit2_discussion.py
```

I used Python 3 and the standard-library `collections` module. On Windows, the equivalent command was `py unit2_discussion.py` when the Python launcher was installed.

| Case tested | Result observed |
| --- | --- |
| Four stack values | Values were removed in reverse insertion order. |
| Four queue values | Values were removed in insertion order. |
| Stack peek and queue front | The previewed value remained available for removal. |
| Empty stack pop and peek | Descriptive `IndexError` exceptions were caught. |
| Empty queue dequeue and front | Descriptive `IndexError` exceptions were caught. |
| Single-item structures | Each structure became empty after removal. |
| Duplicate values | Both copies were retained and removed in the correct order. |
| Zero, empty string, and None | These valid stored values were preserved. |
| Interleaved additions and removals | LIFO and FIFO ordering remained correct. |

The completed run ended with `All ordering, preview, empty, single-item, and extra assertions passed.` I caught expected exceptions around individual operations so the demonstrations continued. Unexpected failures were not silently suppressed. Assertions provided checks when Python ran without optimization.

### Memory behavior and growth

I analyzed each container as using O(n) storage for n item references, with additional memory for the stored objects. Longer text required additional storage. I did not impose a fixed capacity, so the structures could grow until limited by available memory.

I used amortized O(1) list append and end-pop operations for the stack and O(1) deque endpoint operations for the queue. Preview and empty checks took O(1). Using `popleft()` avoided the shifting required by `list.pop(0)`.

### Practical application and design reflection

I demonstrated a text-editor undo history with the stack and a support-desk ticket line with the queue. Each example added four values and displayed their removal order. LIFO matched undoing the newest edit first, while FIFO matched processing tickets in arrival order.

I chose exceptions for empty operations so an empty structure could be distinguished from a valid stored `None`. I accepted arbitrary values in these general-purpose structures; a ticket application could separately validate ticket descriptions. For a larger application, I considered a capacity limit with an explicit full-queue response to control memory growth.

## Submission Status

I completed and locally checked the Python implementation and prepared a separate discussion draft in `discussion_post.md`. I added the repository link to that draft and recorded completed work in `submission_checklist.md`. IntelliJ verification, discussion submission, and two peer responses remained unconfirmed.

## Original Assignment Instructions (Retained)

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
