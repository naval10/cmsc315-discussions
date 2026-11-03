"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


from time import perf_counter


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Inspect items in order; a missing target requires all n checks: O(n).
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Precondition: ascending order with mutually comparable values.
    # Checking sortedness here would add O(n) work to every search.
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        value = lst[mid]
        if value == target:
            return mid
        if value < target:
            # Discard the midpoint and everything below it.
            low = mid + 1
        else:
            # Discard the midpoint and everything above it.
            high = mid - 1
    # Each iteration halves the candidate range: O(log n) worst-case time.
    # An empty list starts with high = -1 and skips the loop.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # TODO: Create a small dataset and test both searches.
    small = [101, 205, 309, 412, 518]
    for target, expected in [(412, 3), (999, -1)]:
        linear = linear_search(small, target)
        binary = binary_search(small, target)
        assert linear == binary == expected
        print(f"Target {target}: linear index={linear}, binary index={binary}")
    # Index 3 identifies 412; -1 means that 999 was not present.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # TODO: Create a larger dataset and compare results.
    large = list(range(100_000))
    for target, expected in [(99_999, 99_999), (100_000, -1)]:
        results = []
        for search in (linear_search, binary_search):
            start = perf_counter()
            for _ in range(100):
                result = search(large, target)
            average_us = (perf_counter() - start) * 1_000_000 / 100
            assert result == expected
            results.append(result)
            print(f"{search.__name__}: target={target}, index={result}, "
                  f"average={average_us:.2f} microseconds (100 runs)")
        assert results[0] == results[1]
    # These late/missing targets require 100,000 linear visits, but at most
    # 17 midpoint visits in binary search. Timing varies by machine and load.
    # Dataset creation and sorting are outside the timed search loops.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # TODO: Demonstrate and explain edge cases.
    cases = [
        ("Empty list", [], 5, -1),
        ("Single item found", [5], 5, 0),
        ("Single item missing", [5], 6, -1),
        ("First position", [2, 4, 6, 8], 2, 0),
        ("Last position", [2, 4, 6, 8], 8, 3),
        ("Below minimum", [2, 4, 6, 8], 1, -1),
        ("Above maximum", [2, 4, 6, 8], 9, -1),
        ("Missing between items", [2, 4, 6, 8], 5, -1),
        ("Negative and zero", [-3, 0, 7], 0, 1),
    ]
    for label, values, target, expected in cases:
        assert linear_search(values, target) == expected
        assert binary_search(values, target) == expected
        print(f"{label}: both searches returned {expected}")
    # Linear search returns the first duplicate; binary may return any match.
    duplicates = [2, 4, 4, 4, 6]
    assert linear_search(duplicates, 4) == 1
    found = binary_search(duplicates, 4)
    assert found in (1, 2, 3) and duplicates[found] == 4
    print(f"Duplicates: linear index=1; binary valid matching index={found}")
    words = ["firewall", "router", "switch"]
    assert linear_search(words, "router") == binary_search(words, "router") == 1
    print("Sorted strings: both searches found router at index 1")

    print("\n=== IT ASSET LOOKUP ===")
    # Arrival order matters during intake, so preserve the original list.
    incoming_ids = [1042, 1007, 1099, 1015, 1063]
    original = incoming_ids.copy()
    target = 1099
    intake_index = linear_search(incoming_ids, target)
    # Pay the sorting cost once, then reuse this index for repeated lookups.
    sorted_ids = sorted(incoming_ids)
    sorted_index = binary_search(sorted_ids, target)
    assert intake_index == 2 and sorted_index == 4
    assert incoming_ids == original
    print(f"Arrival order: {incoming_ids}")
    print(f"Sorted IDs:    {sorted_ids}")
    print(f"Asset {target}: intake index={intake_index}, sorted index={sorted_index}")
    print("Indices refer to different lists; both identify the same asset.")
    print("Linear search suits a one-time scan of unsorted incoming assets.")
    print("Binary search needs sorted data and a consistent comparison rule.")
    print("Both iterative searches use O(1) extra space; the sorted copy uses O(n).")
    print("\nAll small, large, edge-case, and asset lookup assertions passed.")


if __name__ == "__main__":
    main()
