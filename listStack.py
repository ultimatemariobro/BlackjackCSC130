"""

All other code was created by Coleman Pilkington
18 OCT 2022
"""


#######################################
# READ ME!!!!
# check to see if pop is actually popping top index or the number suggested or whatever idrfc
#
#

class ListStack(object):
    """An list-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()
        if sourceCollection:
            for item in sourceCollection:
                self.push(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the stack is empty, or False otherwise."""
        if len(self.items) < 1:
            return True
        else:
            return False

    def __len__(self):
        """Returns the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the stack."""
        # return f"{self.items}"
        # strang = ""
        # for item in self.items:
        #     if item == self.items[0]:
        #         strang += "[" + str(item)
        #     elif item == self.items[-1]:
        #         strang += str(item) + "]"
        #     else:
        #         strang = strang + "," + str(item)
        # return strang

        # code above works, but when adding two stacks together, keeps ] so.. no beuno

        return f"{self.items}"

    # come back to this and add { }'s

    def __iter__(self):
        """Supports iteration over a view of the stack."""
        return iter(self.items)

    def __add__(self, other):
        """Returns a new stack containing the contents
        of self and other."""
        result = ListStack(self)
        for item in other:
            result.push(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self.items == other:
            return True
        else:
            return False

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raises IndexError if stack is not empty."""

        return self.items[-1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = []

    def push(self, item):
        """Inserts item at top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raises IndexError if stack is not empty. ** Think he means if it IS empty...?**
        Postcondition: the top item is removed from the stack."""
        if len(self.items) < 1:
            raise IndexError
        else:
            topIndex = len(self.items) - 1
            popped = self.items[topIndex]
            del self.items[-1]
            return popped