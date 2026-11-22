Repository: https://github.com/naval10/cmsc315-discussions/tree/master/unit7_sorting

I used supplier quotes for the same keyboard to compare bubble sort and merge sort. Both returned [27, 27, 31, 39] and left the original quotes in arrival order. Keeping both $27 quotes mattered because two suppliers could offer the same price.

Bubble sort was easier to trace: I only had to compare neighbors and decide whether to swap them. The trickier part of merge sort was keeping track of two positions. When one half ran out, the other half could still contain several quotes. I handled that by appending the remaining values and checking the entire result against Python’s sorted output.

For a short list that was already in order, bubble sort made one pass with no swaps and stopped. On a long list in reverse order, its work grew quadratically. Merge sort took O(n log n) time because each merge level processed the full set of values, but it needed extra memory for the halves and merged results. I would choose merge sort between these two for a large collection of quotes.
