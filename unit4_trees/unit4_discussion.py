"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self._validate_id(value)
        # Preserve the root returned by the helper, including the first insertion.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)
        # Smaller IDs belong on the left; larger IDs belong on the right.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Equal IDs are ignored because an employee ID should be unique.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        self._validate_id(value)
        # Each comparison eliminates one subtree, not necessarily half the nodes.
        # A short, balanced tree needs fewer comparisons than a linear scan.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # Left values are smaller; right values are larger, giving sorted output.
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


    @staticmethod
    def _validate_id(value):
        # bool is an int subclass, but True/False are not employee IDs.
        if type(value) is not int:
            raise TypeError("Employee ID must be an integer.")
        if value <= 0:
            raise ValueError("Employee ID must be positive.")

    def height(self):
        """Return height in nodes: empty = 0, a single node = 1."""
        def measure(node):
            if node is None:
                return 0
            return 1 + max(measure(node.left), measure(node.right))
        return measure(self.root)

    def search_steps(self, value):
        """Count visited nodes to illustrate the effect of insertion order."""
        self._validate_id(value)
        node = self.root
        steps = 0
        while node is not None:
            steps += 1
            if value == node.value:
                return steps
            node = node.left if value < node.value else node.right
        return steps


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    # Model an employee-ID index, not a complete employee-record database.
    ids = [1004, 1002, 1006, 1001, 1003, 1005, 1007]
    for employee_id in ids:
        tree.insert(employee_id)
    print("Employee IDs inserted:", ids)
    # This insertion order creates short paths through both subtrees.
    print("Height in nodes:", tree.height())

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    ordered = tree.inorder()
    print("Employee IDs in sorted order:", ordered)
    assert ordered == sorted(ids)
    assert tree.height() == 3

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    for employee_id, expected in [(1001, True), (1007, True),
                                  (999, False), (1008, False)]:
        found = tree.search(employee_id)
        print(f"Employee {employee_id}: found = {found}")
        assert found is expected
    assert tree.search(1004)  # Also check the root.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    empty = BST()
    print("Empty traversal:", empty.inorder())
    print("Search empty tree:", empty.search(1001))
    assert empty.inorder() == [] and not empty.search(1001)
    assert empty.height() == 0

    single = BST()
    single.insert(1001)
    single.insert(1001)
    print("Single node after duplicate insertion:", single.inorder())
    assert single.inorder() == [1001] and single.height() == 1
    assert single.search(1001) and not single.search(1002)

    before = tree.inorder()
    tree.insert(1004)
    tree.insert(1001)
    assert tree.inorder() == before
    print("Duplicate root and leaf IDs were ignored.")

    # Invalid requests must fail before changing the existing tree.
    for invalid in [None, "1002", 1002.5, True, 0, -1]:
        expected_error = TypeError if type(invalid) is not int else ValueError
        for operation in [tree.insert, tree.search]:
            try:
                operation(invalid)
            except expected_error as error:
                print(f"{operation.__name__}({invalid!r}): {error}")
            else:
                raise AssertionError("Invalid ID should have been rejected.")
        assert tree.inorder() == before

    # The returned list is a snapshot, not the internal tree.
    snapshot = tree.inorder()
    snapshot.append(9999)
    assert not tree.search(9999)
    tree.insert(1008)
    assert tree.search(1008)
    print("Valid insertion after errors succeeded.")

    print("\n=== INSERTION ORDER AND TREE SHAPE ===")
    balanced = BST()
    ascending = BST()
    descending = BST()
    for employee_id in ids:
        balanced.insert(employee_id)
    for employee_id in sorted(ids):
        ascending.insert(employee_id)
    for employee_id in sorted(ids, reverse=True):
        descending.insert(employee_id)
    assert balanced.inorder() == ascending.inorder() == descending.inorder()
    assert balanced.height() == 3
    assert ascending.height() == descending.height() == 7
    print("Same IDs, balanced-order height:", balanced.height())
    print("Same IDs, ascending-order height:", ascending.height())
    print("Same IDs, descending-order height:", descending.height())
    print("Search 1007, balanced-order nodes visited:", balanced.search_steps(1007))
    print("Search 1007, ascending-order nodes visited:", ascending.search_steps(1007))
    assert balanced.search_steps(1007) == 3
    assert ascending.search_steps(1007) == 7
    assert descending.search_steps(1001) == 7
    print("This BST does not rebalance; long chains can reach Python's recursion limit.")
    print("\nAll BST checks passed.")



if __name__ == "__main__":
    main()
