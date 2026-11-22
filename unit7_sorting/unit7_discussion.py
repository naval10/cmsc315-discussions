"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    result = lst.copy()
    for end in range(len(result)-1, 0, -1):
        changed = False
        for i in range(end):
            # Move the larger neighbor toward the sorted suffix.
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
                changed = True
        if not changed:
            break
    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    if len(lst) < 2:
        return lst.copy()
    mid = len(lst)//2
    # Each recursive call handles a strictly smaller list.
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Taking the left item on ties preserves the original tie order.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def compare(values):
    original = values.copy()
    bubble, merged = bubble_sort(values), merge_sort(values)
    print("Original:", original, "| Bubble:", bubble, "| Merge:", merged)
    assert bubble == merged == sorted(original)
    assert values == original


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    # TODO: Create an unsorted dataset and test both sorting algorithms.
    compare([42, 19, 88, 7, 31, 12, 55])

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    # TODO: Create a second dataset and compare sorting results.
    compare([76, 24, 61, 11, 39, 24, 15])

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # TODO: Demonstrate and explain edge cases.
    for label, values in [("Empty: nothing to move", []), ("Singleton: already sorted", [8]),
                          ("Sorted: bubble stops after one pass", [1, 2, 3]),
                          ("Reverse: every pair is inverted", [3, 2, 1]),
                          ("Duplicates: both copies survive", [4, 1, 4])]:
        print(label)
        compare(values)
    print("Supplier quotes for the same keyboard, lowest first:")
    compare([39, 27, 31, 27])
    print("All checks passed.")




if __name__ == "__main__":
    main()
