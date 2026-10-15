# Unit 1: Network Device and Firewall Example


## Completed Implementation

I used a home-network scenario to represent a general network device and a specialized firewall. I retained the starter class names and all original TODO prompts so the completed work could be compared with the requirements. The program modeled configuration data; it did not connect to or control a real firewall.

### Classes, inheritance, and encapsulation

- I implemented `ParentClass` with the class variable `category`, the instance variables `_name` and `_location`, and the constructor `__init__`.
- I implemented `describe()` to summarize a device and `__str__()` to support readable printed objects.
- I derived `ChildClass` from `ParentClass`, called `super().__init__()`, and added the class variable `device_type` and instance variables `_mode` and `_settings`.
- I overrode `describe()` and reused the parent description with `super().describe()`.
- I added `add_rule()`, `remove_rule()`, and `__len__()`. The removal method served as my student-created extension, which I labeled TODO 6 because the starter contained only five numbered TODO blocks.
- I used underscore-prefixed attributes to indicate internal data. These names provided a convention, not enforced privacy. I exposed rules through a read-only property that returned a tuple snapshot, and I used methods to validate modifications. The special methods supported standard object operations; they did not enforce privacy by themselves.

### Namespaces and copying

I created two firewall objects, accessed `device_type` through the class and an object, and added `owner` to only the first object. I printed both instance dictionaries and the child class namespace keys. I also showed that `category` belonged to the parent class namespace and was inherited by the child.

I stored a mutable rule list inside the `_settings` dictionary. I made a shallow copy and a deep copy before modifying the original list. The original and shallow copy both displayed the new rule because they shared nested data. The deep copy retained the earlier rule list. I used identity checks and assertions to verify this distinction. Separate objects created normally had separate dictionaries and lists.

### Error handling and testing

I ran the original starter, which printed placeholders, and then ran the completed program with:

```bash
python3 unit1_discussion.py
```

I used Python 3 and only the standard-library `copy` module. On Windows, the equivalent command was `py unit1_discussion.py` when the Python launcher was installed.

The completed run ended with `All checks passed.` I tested the following cases:

| Case tested | Result observed |
| --- | --- |
| Empty rule list | The object displayed an empty list and had length zero. |
| Valid additions and removal | Rules were added in order, and the requested rule was removed. |
| Blank name or rule | A `ValueError` was caught and explained. |
| Missing location or non-text rule | A `TypeError` was caught and explained. |
| Invalid mode | A `ValueError` was caught. |
| Duplicate rule | A `ValueError` was caught; no duplicate was added. |
| Removal of a missing rule, including an empty list | A `ValueError` was caught; existing data was preserved. |
| Whitespace around a valid rule | The whitespace was removed before storage. |
| Public rule snapshot | The previously returned tuple remained unchanged after another addition. |
| Recovery after errors | A later valid rule was added successfully. |
| Copy behavior | Shallow data was shared, and deep data was independent. |

I caught the expected exceptions around individual demonstration operations, so one invalid request did not stop later operations. Unexpected failures were not silently suppressed. Assertions supplied additional checks when the script ran without Python's optimization option.

### Memory behavior and growth

I used a dictionary containing a list of rule strings. For `n` rules of bounded length, each firewall's rule storage grew linearly, O(n). Including string contents, storage depended on the total text length as well as the list references. Class variables were stored on their defining classes rather than duplicated in every instance dictionary.

The duplicate check in `add_rule()` took O(n) comparisons; the list append itself had amortized O(1) cost. Finding and removing a rule took O(n) time. String comparisons also depended on string length. `len()` took O(1) time, while the `rules` property built an O(n) tuple snapshot. Displaying the object also traversed its rules.

For this fixed set of attributes, a shallow object copy added O(1) storage relative to the rule count and shared the nested settings. A deep copy rebuilt the mutable dictionary and list in O(n) time and space for this model; immutable strings could be reused. I accepted the extra copying cost when an independent configuration snapshot was needed. I kept a list for readability and ordering; for a much larger rule collection, I considered an additional set for faster membership checks, at the cost of more memory and synchronization work.

### Practical application and design reflection

I connected the example to home networking and my interest in cybersecurity. A firewall reused general device information while adding specialized rule operations. Encapsulation concentrated validation in one place, and inheritance avoided repeating the device setup. The design could have supported future monitoring tools with additional device subclasses. For a small one-time task, procedural functions would have required less structure; for related device types, the class design made maintenance and reuse easier.

### Deciding when shared data was acceptable

I based my decision on whether a change was supposed to affect both objects. Sharing immutable strings, such as device labels and rule text, was acceptable because those strings could not be changed in place. Assigning a different string to one object's attribute did not rewrite the string referenced by another object.

I treated the mutable rule list differently. A shallow copy was acceptable for demonstrating two objects that intentionally referenced the same current configuration. In that situation, seeing a new rule through both objects was expected. However, I did not treat a shallow copy as an independent backup or a separate firewall configuration. Adding or removing a rule through either copy changed their shared list, which could create unintended configuration changes if the objects were assumed to be independent.

For a configuration snapshot or a trial change, I chose a deep copy so the nested dictionary and list were independent. In the demonstration, adding a rule to the original also changed the shallow copy, while the deep copy kept its earlier rules. Those results and the identity checks confirmed why independence mattered. Separately constructed firewall objects also received their own settings and rule lists.

I balanced that isolation against memory and copying costs. I accepted the additional storage for an independent mutable configuration when preserving earlier settings mattered. For read-only access to the rules, I used the existing tuple snapshot instead of copying the entire object. Because the tuple contained immutable strings, it let callers inspect the rules without modifying the internal list. This helped me distinguish three needs: intentionally shared current data, a stable read-only view, and an independently editable copy.

## Submission Status

I completed and locally checked the Python implementation and prepared a discussion draft in `discussion_post.md`. I added the repository link to the discussion draft. Discussion submission and two peer responses remained pending.

## Original Assignment Instructions (Retained)

# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.