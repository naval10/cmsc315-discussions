"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    # TODO: Create a dictionary and add multiple key-value pairs.
    # Each immutable SKU identifies one equipment type and its stock count.
    # A dictionary hashes keys to locate entries instead of scanning all keys.
    inventory = {}
    for sku, quantity in [
        ("ROUTER-01", 5), ("SWITCH-01", 8), ("LAPTOP-01", 12),
        ("MONITOR-01", 6), ("CABLE-01", 30)
    ]:
        inventory[sku] = quantity
    assert len(inventory) == 5
    print("IT supply inventory:", inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # TODO: Demonstrate successful key lookups.
    # Known keys can be indexed directly; a missing key would raise KeyError.
    for sku, expected in [("ROUTER-01", 5), ("LAPTOP-01", 12)]:
        quantity = inventory[sku]
        assert quantity == expected
        print(f"{sku}: {quantity} in stock")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    # TODO: Demonstrate updating an existing key.
    print("Before update:", inventory)
    old_size = len(inventory)
    # Reassigning an equal key replaces its value without creating a duplicate.
    inventory["LAPTOP-01"] = 10
    assert inventory["LAPTOP-01"] == 10
    assert len(inventory) == old_size
    print("After issuing two laptops:", inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    # TODO: Demonstrate deleting a key-value pair.
    print("Before deletion:", inventory)
    # pop removes both the key and value and returns the removed quantity.
    removed = inventory.pop("MONITOR-01")
    assert removed == 6 and "MONITOR-01" not in inventory
    assert len(inventory) == 4
    print(f"Removed MONITOR-01 with recorded quantity {removed}.")
    print("After deletion:", inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # TODO: Demonstrate and explain edge cases.
    # A unique sentinel distinguishes absence from valid values such as zero.
    missing = object()
    before = inventory.copy()
    assert inventory.get("PRINTER-99", missing) is missing
    assert inventory == before
    print("Missing lookup: PRINTER-99 was not found; inventory unchanged.")

    assert inventory.pop("PRINTER-99", missing) is missing
    assert inventory == before
    print("Missing deletion: safely skipped; inventory unchanged.")

    # Assignment to a new key inserts an entry, even if described as an update.
    inventory["HEADSET-01"] = 3
    assert inventory["HEADSET-01"] == 3 and len(inventory) == 5
    print("Assigning missing HEADSET-01 inserted a new entry.")

    # Zero means out of stock, not a missing equipment type.
    inventory["CABLE-01"] = 0
    quantity = inventory.get("CABLE-01", missing)
    assert quantity == 0 and quantity is not missing
    print("CABLE-01 exists with zero stock; it is not a missing key.")

    empty = {}
    assert empty.get("ROUTER-01", missing) is missing
    assert empty.pop("ROUTER-01", missing) is missing
    assert len(empty) == 0
    print("Empty inventory: lookup and deletion safely reported no entry.")

    # Mutable lists cannot be dictionary keys; catch the expected TypeError.
    before = inventory.copy()
    try:
        inventory[["BAD-SKU"]] = 1
    except TypeError:
        print("Invalid list key: TypeError handled; use an immutable SKU.")
    else:
        raise AssertionError("An unhashable list key should be rejected.")
    assert inventory == before

    print("Final inventory:", inventory)
    print("\nAll insertion, lookup, update, deletion, and edge-case assertions passed.")



if __name__ == "__main__":
    main()
