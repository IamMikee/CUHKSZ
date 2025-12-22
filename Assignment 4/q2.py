# Question 2: Undo/Redo Text Editor with Limited Memory
# Please DO NOT modify the given code except the TODO part
# You may add your own helper functions if necessary


class Stack:
    """A simple Stack implementation using Python list."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item. Returns None if empty."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Return the top item without removing it. Returns None if empty."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def clear(self):
        """Remove all items from the stack."""
        self.items = []

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


class LimitedStack:
    """
    A Stack with maximum capacity.
    When full, the oldest (bottom) item is removed to make room for new items.
    This behaves like a combination of Stack and Queue.
    """
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        """
        Push an item onto the stack.
        If at max capacity, remove the oldest (bottom) item first.
        """
        if len(self.items) >= self.max_size:
            self.items.pop(0)  # Remove oldest item (bottom of stack)
        self.items.append(item)

    def pop(self):
        """Remove and return the top item. Returns None if empty."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Return the top item without removing it. Returns None if empty."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def clear(self):
        """Remove all items from the stack."""
        self.items = []

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


class TextEditor:
    """
    A text editor with undo/redo functionality and limited undo history.

    The editor maintains:
    - A document (string)
    - An undo history (LimitedStack) storing operations as tuples
    - A redo history (Stack) storing operations as tuples

    Operations are stored as: ("type", text) or ("delete", deleted_text)
    """
    def __init__(self, max_undo=10):
        """
        Initialize the text editor.

        parameter max_undo: int, maximum number of operations that can be undone
        """
        self.document = ""
        self.undo_stack = LimitedStack(max_undo)
        self.redo_stack = Stack()

    def type(self, text):
        """
        Append text to the document.

        Steps:
        1. Save the operation ("type", text) to undo_stack
        2. Append text to document
        3. Clear redo_stack (new action clears redo history)

        parameter text: string, text to append
        return: None
        """
        # TODO part
        # ------- Your code start here -------



        # ------- End of your code -----------

    def delete(self, n):
        """
        Delete the last n characters from the document.

        Steps:
        1. Calculate actual characters to delete (min of n and document length)
        2. Extract the text that will be deleted
        3. Save the operation ("delete", deleted_text) to undo_stack
        4. Remove the characters from document
        5. Clear redo_stack

        parameter n: int, number of characters to delete
        return: None
        """
        # TODO part
        # ------- Your code start here -------



        # ------- End of your code -----------

    def undo(self):
        """
        Undo the last operation.

        Steps:
        1. If undo_stack is empty, return current document (nothing to undo)
        2. Pop operation from undo_stack
        3. If it was ("type", text): remove that text from end of document
        4. If it was ("delete", text): add that text back to end of document
        5. Push the REVERSE operation to redo_stack
           - "type" becomes "delete" in redo
           - "delete" becomes "type" in redo

        return: string, the document content after undo
        """
        # TODO part
        # ------- Your code start here -------



        # ------- End of your code -----------

    def redo(self):
        """
        Redo the last undone operation.

        Steps:
        1. If redo_stack is empty, return current document (nothing to redo)
        2. Pop operation from redo_stack
        3. If it was ("type", text): add that text to document
        4. If it was ("delete", text): remove that text from document
        5. Push the REVERSE operation to undo_stack

        return: string, the document content after redo
        """
        # TODO part
        # ------- Your code start here -------



        # ------- End of your code -----------

    def get_document(self):
        """
        Return the current document content.

        return: string, the current document
        """
        return self.document


# Test cases
if __name__ == '__main__':
    print("=" * 50)
    print("Test Case 1: Basic type and undo")
    print("=" * 50)
    editor1 = TextEditor(max_undo=5)
    editor1.type("Hello")
    print(f"After type 'Hello': '{editor1.get_document()}'")  # Expected: Hello
    editor1.type(" World")
    print(f"After type ' World': '{editor1.get_document()}'")  # Expected: Hello World
    print(f"Undo: '{editor1.undo()}'")  # Expected: Hello
    print(f"Undo: '{editor1.undo()}'")  # Expected: (empty string)
    print()

    print("=" * 50)
    print("Test Case 2: Delete and undo")
    print("=" * 50)
    editor2 = TextEditor(max_undo=5)
    editor2.type("ABCDEF")
    print(f"After type 'ABCDEF': '{editor2.get_document()}'")  # Expected: ABCDEF
    editor2.delete(3)
    print(f"After delete 3: '{editor2.get_document()}'")  # Expected: ABC
    print(f"Undo: '{editor2.undo()}'")  # Expected: ABCDEF
    print()

    print("=" * 50)
    print("Test Case 3: Redo functionality")
    print("=" * 50)
    editor3 = TextEditor(max_undo=5)
    editor3.type("Test")
    editor3.type("ing")
    print(f"Document: '{editor3.get_document()}'")  # Expected: Testing
    print(f"Undo: '{editor3.undo()}'")  # Expected: Test
    print(f"Redo: '{editor3.redo()}'")  # Expected: Testing
    print()

    print("=" * 50)
    print("Test Case 4: New action clears redo history")
    print("=" * 50)
    editor4 = TextEditor(max_undo=5)
    editor4.type("ABC")
    editor4.type("DEF")
    editor4.undo()  # Back to ABC
    editor4.type("XYZ")  # This should clear redo history
    print(f"Document: '{editor4.get_document()}'")  # Expected: ABCXYZ
    print(f"Redo (should have nothing): '{editor4.redo()}'")  # Expected: ABCXYZ (no change)
    print()

    print("=" * 50)
    print("Test Case 5: Limited undo history")
    print("=" * 50)
    editor5 = TextEditor(max_undo=3)  # Can only undo last 3 operations
    editor5.type("A")
    editor5.type("B")
    editor5.type("C")
    editor5.type("D")  # This pushes out the first operation
    print(f"Document: '{editor5.get_document()}'")  # Expected: ABCD
    print(f"Undo 1: '{editor5.undo()}'")  # Expected: ABC
    print(f"Undo 2: '{editor5.undo()}'")  # Expected: AB
    print(f"Undo 3: '{editor5.undo()}'")  # Expected: A
    print(f"Undo 4 (nothing left): '{editor5.undo()}'")  # Expected: A (can't undo first 'A')
    print()

    print("=" * 50)
    print("Test Case 6: Delete more than document length")
    print("=" * 50)
    editor6 = TextEditor(max_undo=5)
    editor6.type("Hi")
    editor6.delete(100)  # Try to delete 100 chars but only 2 exist
    print(f"Document after delete 100: '{editor6.get_document()}'")  # Expected: (empty)
    print(f"Undo: '{editor6.undo()}'")  # Expected: Hi
