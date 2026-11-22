# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

## Implementation and verification

Both algorithms returned sorted copies. Two datasets, five edge cases, and a supplier quote example matched Python’s sorted output without modifying their inputs. Run `python unit7_discussion.py` in this folder.

I used supplier quotes for the same keyboard to compare bubble sort and merge sort. Both returned [27, 27, 31, 39] and left the original quotes in arrival order. Keeping both $27 quotes mattered because two suppliers could offer the same price.

Bubble sort was easier to trace: I only had to compare neighbors and decide whether to swap them. The trickier part of merge sort was keeping track of two positions. When one half ran out, the other half could still contain several quotes. I handled that by appending the remaining values and checking the entire result against Python’s sorted output.

For a short list that was already in order, bubble sort made one pass with no swaps and stopped. On a long list in reverse order, its work grew quadratically. Merge sort took O(n log n) time because each merge level processed the full set of values, but it needed extra memory for the halves and merged results. I would choose merge sort between these two for a large collection of quotes.
