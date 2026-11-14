# Unit 6 Discussion Post

Repository: https://github.com/naval10/cmsc315-discussions

Unit 6 files: https://github.com/naval10/cmsc315-discussions/tree/master/unit6_hash_tables

## Design Approach

I used a dictionary to manage an IT supply inventory. Equipment codes such as ROUTER-01 served as keys, and stock quantities served as values. My program inserted five entries, retrieved two quantities, updated laptop stock, and removed a monitor entry. Assertions checked the results and confirmed that updating an existing key did not create a duplicate entry.

I handled missing lookups and deletions using a unique sentinel. This mattered because zero stock was a valid value, not evidence that an equipment code was missing. I also tested an empty dictionary, assignment to a new key, and an invalid mutable list key. All assertions passed in the development environment.

Hash tables use hashes to help locate entries. When different keys map to the same table position, a collision occurs. The implementation must resolve that collision and compare keys so that distinct entries remain accessible. Python handled that process internally in my program. Typical dictionary operations have average O(1) time, but worst-case operations can take O(n). Storage grows with the number of entries and includes table overhead.

## Reflection

I used a Python dictionary to model an IT supply inventory, with equipment codes as keys and stock quantities as values. I practiced inserting records, looking up quantities, updating existing entries, and removing an equipment type. Using unique codes made the relationship between a key and its value easy to follow.

The main challenge was distinguishing a missing item from an item with zero stock. A simple truth-value check could treat both situations alike. I used a unique sentinel with get and pop so the program could report missing keys without confusing them with valid quantities. I also checked an empty dictionary and caught the TypeError caused by attempting to use a mutable list as a key.

I learned that hash tables use a key’s hash to help locate an entry. Collisions occur when different keys map to the same table position, so the implementation must resolve them and compare keys. Dictionary operations generally take average O(1) time, but collisions can make worst-case operations O(n). For repeated inventory lookups, this approach avoided scanning every record, although the table required additional memory.
