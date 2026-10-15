"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending puts the newest value at the top for LIFO removal.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        # Read the newest item without changing the stack.
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return not self._items


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Add at the back so older values remain first in line.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")
        # Read the oldest item without removing it.
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return not self._items



def expect_empty_error(label, operation):
    """Verify that an invalid removal or preview raises a clear error."""
    try:
        operation()
    except IndexError as error:
        print(f"{label}: {error}")
    else:
        raise AssertionError(f"{label} should have raised IndexError.")


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: TEXT EDITOR UNDO ===")
    stack = Stack()
    actions = ["Typed title", "Added paragraph", "Bolded heading", "Inserted image"]
    for action in actions:
        stack.push(action)
        print("Recorded:", action)
    print("Peek without removal:", stack.peek())
    assert stack.peek() == actions[-1]
    undone = []
    while not stack.is_empty():
        undone.append(stack.pop())
        print("Undo:", undone[-1])
    assert undone == list(reversed(actions))
    expect_empty_error("Pop empty stack", stack.pop)
    expect_empty_error("Peek empty stack", stack.peek)
    stack.push("Single edit")
    assert stack.pop() == "Single edit"
    assert stack.is_empty()
    print("Single-item stack became empty:", stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: SUPPORT DESK TICKETS ===")
    queue = Queue()
    tickets = ["Reset password", "Install printer", "Update software", "Fix Wi-Fi"]
    for ticket in tickets:
        queue.enqueue(ticket)
        print("Ticket added:", ticket)
    print("Front without removal:", queue.front())
    assert queue.front() == tickets[0]
    processed = []
    while not queue.is_empty():
        processed.append(queue.dequeue())
        print("Processed:", processed[-1])
    assert processed == tickets
    expect_empty_error("Dequeue empty queue", queue.dequeue)
    expect_empty_error("Front of empty queue", queue.front)
    queue.enqueue("Single ticket")
    assert queue.dequeue() == "Single ticket"
    assert queue.is_empty()
    print("Single-item queue became empty:", queue.is_empty())

    # Extra tests: interleaved operations, duplicates, and valid falsy values.
    for structure, add, remove, preview in [
        (Stack(), "push", "pop", "peek"),
        (Queue(), "enqueue", "dequeue", "front"),
    ]:
        for value in [0, "", None, "repeat", "repeat"]:
            getattr(structure, add)(value)
        expected = [0, "", None, "repeat", "repeat"]
        if isinstance(structure, Stack):
            expected.reverse()
        assert getattr(structure, preview)() == expected[0]
        assert [getattr(structure, remove)() for _ in expected] == expected
        assert structure.is_empty()

    stack.push("A")
    stack.push("B")
    assert stack.pop() == "B"
    stack.push("C")
    assert [stack.pop(), stack.pop()] == ["C", "A"]
    queue.enqueue("A")
    queue.enqueue("B")
    assert queue.dequeue() == "A"
    queue.enqueue("C")
    assert [queue.dequeue(), queue.dequeue()] == ["B", "C"]
    print("\nAll ordering, preview, empty, single-item, and extra assertions passed.")


if __name__ == "__main__":
    main()
