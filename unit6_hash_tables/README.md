# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.


## Completed Implementation

I completed all five student TODO sections and retained the original prompts and instruction comments. I chose an IT supply inventory, with immutable string SKUs as keys and integer stock counts as values. I used Python's dictionary implementation rather than building a separate hash table.

### Running the program

From the repository root:

```bash
python unit6_hash_tables/unit6_discussion.py
```

I ran the starter before modifying it; it printed placeholder messages. I then ran the completed program with assertions enabled in the development environment. It ended with:

```text
All insertion, lookup, update, deletion, and edge-case assertions passed.
```

### Operations and evidence

| Requirement | What I implemented and checked |
| --- | --- |
| Create and insert | I created an empty dictionary, inserted five SKU/quantity pairs, and asserted its size. |
| Lookup | I retrieved ROUTER-01 and LAPTOP-01 and asserted quantities 5 and 12. |
| Update | I changed LAPTOP-01 to 10 and verified that the number of keys stayed the same. |
| Delete | I removed MONITOR-01 with pop, checked its returned value, and verified its absence. |
| Missing lookup and deletion | I used a unique sentinel and verified that neither operation changed the dictionary. |
| Assignment to a missing key | I inserted HEADSET-01 and checked the new size. |
| Zero stock | I verified that CABLE-01 existed with quantity 0, separately from a missing entry. |
| Empty dictionary | I checked safe lookup and deletion without inserting anything. |
| Invalid key | I caught TypeError for a mutable list key and verified that the dictionary was unchanged. |

### Hashing and efficiency

I explained that a dictionary used hashes to help locate entries and key equality to identify the correct record. Different keys could map to the same table position, causing a collision. Collision resolution allowed those keys to coexist; a collision did not mean that one value should overwrite the other. Reassigning an equal key, by contrast, intentionally replaced its value. I relied on Python to resolve collisions internally; I did not claim that the SKU examples forced a collision.

I described lookup, insertion, update, and deletion as average O(1) operations under typical hashing assumptions. Individual operations could take O(n) in the worst case, and resizing could make an insertion more expensive. The table used O(n) storage for n entries, with extra capacity and bookkeeping beyond the values themselves. I treated key hashing and equality as bounded-cost operations for these short SKUs.

I chose a dictionary for repeated exact-key inventory queries. A list scan would require O(n) worst-case lookup, while a dictionary avoided scanning every record on average. I noted that fast key access did not automatically provide fast searches by quantity or sorted ranges.

### Design limits

I used controlled sample quantities. The demo did not validate interactive input, prevent negative stock, persist records, or support concurrent updates. A production version would need those features. I also kept SKU spelling consistent because different capitalization could identify different string keys.

## Completed Reflection

I used a Python dictionary to model an IT supply inventory, with equipment codes as keys and stock quantities as values. I practiced inserting records, looking up quantities, updating existing entries, and removing an equipment type. Using unique codes made the relationship between a key and its value easy to follow.

The main challenge was distinguishing a missing item from an item with zero stock. A simple truth-value check could treat both situations alike. I used a unique sentinel with get and pop so the program could report missing keys without confusing them with valid quantities. I also checked an empty dictionary and caught the TypeError caused by attempting to use a mutable list as a key.

I learned that hash tables use a key’s hash to help locate an entry. Collisions occur when different keys map to the same table position, so the implementation must resolve them and compare keys. Dictionary operations generally take average O(1) time, but collisions can make worst-case operations O(n). For repeated inventory lookups, this approach avoided scanning every record, although the table required additional memory.
