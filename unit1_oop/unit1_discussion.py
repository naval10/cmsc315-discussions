"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    """Represent a network device with a name and location."""

    category = "Network device"

    def __init__(self, name, location):
        self._name = self._validate_text(name, "Name")
        self._location = self._validate_text(location, "Location")

    @staticmethod
    def _validate_text(value, label):
        if not isinstance(value, str):
            raise TypeError(f"{label} must be text.")
        if not value.strip():
            raise ValueError(f"{label} cannot be empty.")
        return value.strip()

    def describe(self):
        return f"{self._name} in {self._location}"

    def __str__(self):
        return self.describe()


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    """Represent a firewall; this example does not configure real devices."""

    device_type = "Firewall"

    def __init__(self, name, location, mode="monitor"):
        super().__init__(name, location)
        if mode not in ("monitor", "enforce"):
            raise ValueError("Mode must be monitor or enforce.")
        self._mode = mode
        # Each instance receives its own nested mutable data.
        self._settings = {"rules": []}

    @property
    def rules(self):
        # An immutable snapshot prevents changes through the public interface.
        return tuple(self._settings["rules"])

    def add_rule(self, rule):
        rule = self._validate_text(rule, "Rule")
        if rule in self._settings["rules"]:
            raise ValueError(f"Rule already exists: {rule}")
        self._settings["rules"].append(rule)

    def describe(self):
        return (f"{super().describe()} | {self.device_type} | "
                f"mode: {self._mode} | rules: {list(self.rules)}")

    def __len__(self):
        return len(self._settings["rules"])

    # TODO 6 (student-created extension): Remove a rule safely.
    def remove_rule(self, rule):
        rule = self._validate_text(rule, "Rule")
        if rule not in self._settings["rules"]:
            raise ValueError(f"Rule not found: {rule}")
        self._settings["rules"].remove(rule)


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    first = ChildClass("Home firewall", "Living room")
    second = ChildClass("Lab firewall", "Office")
    print("Through class:", ChildClass.device_type)
    print("Through object:", first.device_type)
    first.owner = "Home user"
    print("First instance namespace:", first.__dict__)
    print("Second instance namespace:", second.__dict__)
    print("Second has owner:", hasattr(second, "owner"))
    print("Child class namespace keys:", sorted(ChildClass.__dict__))
    print("Inherited class variable:", ChildClass.category)
    print("category belongs to parent namespace:",
          "category" in ParentClass.__dict__)
    assert "owner" not in second.__dict__
    assert "device_type" not in first.__dict__


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = ChildClass("Main firewall", "Home")
    original.add_rule("Allow HTTPS")
    shallow = copy(original)
    deep = deepcopy(original)
    original.add_rule("Block unknown inbound traffic")

    # A shallow copy is a new object but shares the settings dictionary/list.
    # A deep copy recursively copies that data, so later edits are independent.
    print("Original:", original)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)
    print("Shallow shares settings:", shallow._settings is original._settings)
    print("Deep shares settings:", deep._settings is original._settings)
    assert shallow is not original
    assert shallow._settings is original._settings
    assert deep._settings is not original._settings
    assert deep._settings["rules"] is not original._settings["rules"]
    assert len(shallow) == 2 and len(deep) == 1


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    parent = ParentClass("Router", "Living room")
    print("Parent:", parent)
    assert parent.describe() == "Router in Living room"

    child = ChildClass("Home firewall", "Office", "enforce")
    print("Child with empty rules:", child)
    assert isinstance(child, ParentClass)
    assert len(child) == 0
    child.add_rule("Allow HTTPS")
    child.add_rule("Allow DNS")
    print("Child after adding rules:", child)
    assert child.rules == ("Allow HTTPS", "Allow DNS")
    child.remove_rule("Allow DNS")
    assert child.rules == ("Allow HTTPS",)
    print("Child after removing a rule:", child)

    other = ChildClass("Separate firewall", "Lab")
    assert len(other) == 0  # Ordinary instances do not share their rule lists.
    snapshot = child.rules
    child.add_rule("Block unknown inbound traffic")
    assert snapshot == ("Allow HTTPS",)

    print("\n=== Edge Cases ===")
    cases = [
        ("Empty name", lambda: ParentClass("  ", "Home"), ValueError),
        ("Missing location", lambda: ParentClass("Router", None), TypeError),
        ("Invalid mode", lambda: ChildClass("FW", "Home", "invalid"), ValueError),
        ("Empty rule", lambda: child.add_rule("  "), ValueError),
        ("Non-text rule", lambda: child.add_rule(42), TypeError),
        ("Duplicate rule", lambda: child.add_rule("Allow HTTPS"), ValueError),
        ("Missing rule", lambda: child.remove_rule("Unknown"), ValueError),
        ("Remove from empty list", lambda: other.remove_rule("Allow DNS"), ValueError),
    ]
    before = child.rules
    for label, operation, expected_error in cases:
        try:
            operation()
        except expected_error as error:
            print(f"{label}: handled - {error}")
        else:
            raise AssertionError(f"{label}: expected {expected_error.__name__}")
    assert child.rules == before
    assert len(other) == 0
    child.add_rule("  Allow SSH  ")
    assert child.rules[-1] == "Allow SSH"
    print("Valid operation after errors: added Allow SSH successfully.")

    demonstrate_namespaces()
    demonstrate_copying()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()