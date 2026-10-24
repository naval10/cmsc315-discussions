"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    if type(index) is not int:
        raise TypeError("Insertion index must be an integer.")
    # Keep Python's insert behavior: negative indices count from the end,
    # and out-of-range integer indices are clamped to the nearest endpoint.
    # Existing references at/after the position shift right: O(n) worst case.
    # End insertion is amortized O(1), although resizing can cost O(n).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Accept Python-style negative indices, but reject nonintegers and bool.
    # Invalid deletion returns None without changing the list or crashing.
    if type(index) is not int or not -len(lst) <= index < len(lst):
        return None
    # Removing near the front shifts later references left; end-pop avoids this.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Scan sequentially because the list is not sorted; return the first match.
    # An absent value may require comparing every element: O(n) comparisons.
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Model an IT maintenance checklist whose order can be edited.
    tasks = ["Check backups", "Update software", "Review logs"]
    print("Original maintenance tasks:", tasks)
    insert_at(tasks, 0, "Check alerts")  # Add an urgent task first.
    print("After beginning insertion:", tasks)
    assert tasks == ["Check alerts", "Check backups", "Update software", "Review logs"]
    insert_at(tasks, len(tasks) // 2, "Scan devices")
    print("After middle insertion:", tasks)
    assert tasks == ["Check alerts", "Check backups", "Scan devices",
                     "Update software", "Review logs"]
    insert_at(tasks, len(tasks), "Document results")
    print("After end insertion:", tasks)
    assert tasks[-1] == "Document results"

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    removed = delete_at(tasks, 0)
    print("Removed beginning task:", removed, "| Remaining:", tasks)
    assert removed == "Check alerts"
    removed = delete_at(tasks, len(tasks) // 2)
    print("Removed middle task:", removed, "| Remaining:", tasks)
    assert removed == "Update software"
    removed = delete_at(tasks, len(tasks) - 1)
    print("Removed end task:", removed, "| Remaining:", tasks)
    assert removed == "Document results"
    assert tasks == ["Check backups", "Scan devices", "Review logs"]

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    for task in ["Scan devices", "Replace router"]:
        position = search_value(tasks, task)
        # A missing result of -1 is a sentinel, not a usable list index.
        if position == -1:
            print(f"{task!r}: not found")
        else:
            print(f"{task!r}: found at index {position}")
    assert search_value(tasks, "Scan devices") == 1
    assert search_value(tasks, "Replace router") == -1

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    empty = []
    assert delete_at(empty, 0) is None
    assert search_value(empty, "Task") == -1
    print("Empty deletion returned None; empty search returned -1.")
    insert_at(empty, 0, "Single task")
    assert empty == ["Single task"]
    assert delete_at(empty, 0) == "Single task" and empty == []
    print("Empty insertion and single-item deletion passed.")

    # Invalid requests must preserve the original contents.
    before = tasks.copy()
    for index in [len(tasks), -len(tasks) - 1, "1", 1.5, None, True]:
        assert delete_at(tasks, index) is None
        assert tasks == before
    print("Invalid deletion indices returned None without changing tasks.")

    bounds = ["A", "B", "C"]
    assert delete_at(bounds, -1) == "C"
    assert delete_at(bounds, -len(bounds)) == "A"
    assert bounds == ["B"]
    print("Negative indices correctly removed the last and first items.")

    # Native list insertion clamps extreme integer indices.
    insert_at(bounds, -100, "First")
    insert_at(bounds, 100, "Last")
    insert_at(bounds, -1, "Before last")
    assert bounds == ["First", "B", "Before last", "Last"]
    print("Negative and out-of-range insertion:", bounds)
    for index in ["0", 0.5, None, True]:
        before = bounds.copy()
        try:
            insert_at(bounds, index, "Invalid")
        except TypeError as error:
            print(f"Insertion index {index!r}: {error}")
        else:
            raise AssertionError("Invalid insertion index was accepted.")
        assert bounds == before

    # Repeated tasks are valid; linear search returns the first occurrence.
    repeated = ["Review logs", "Check backups", "Review logs"]
    assert search_value(repeated, "Review logs") == 0
    assert delete_at(repeated, 0) == "Review logs"
    assert search_value(repeated, "Review logs") == 1
    print("Duplicate search returned the first matching index.")

    # Generic helpers allow None, zero, and empty strings as stored values.
    special = [None, 0, ""]
    assert search_value(special, None) == 0
    assert search_value(special, 0) == 1
    assert search_value(special, "") == 2
    assert delete_at(special, 0) is None and special == [0, ""]
    print("Stored None was removed; contents verified despite the None sentinel.")

    insert_at(tasks, len(tasks), "Confirm completion")
    assert search_value(tasks, "Confirm completion") == len(tasks) - 1
    print("Valid operation after errors:", tasks)
    print("\nAll list checks passed.")



if __name__ == "__main__":
    main()