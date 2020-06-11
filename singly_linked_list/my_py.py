class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(slef):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input node in a value
        new_node = Node(value, None)
        # check if there is no head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # what if there is no head
        if self.head is None:
            return None
        # if the head has no next then there is a single element in a list
        if self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_value()
        return value

    def remove_tail(self):
        if self.tail is None:
            return None
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
        current = self.head
        # keeps looking until the node before tail reached
        while current.get_next() != self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value

    def contains(self, value):
        if self.head is None:
            return False
        # get a reference to the node we're currently st, update this as we traverse thru
        current = self.head
        # check to see if we are at valid node
        while current:
            # return true if current value matches our target value
            if current.get_value() == value:
                return True
            # here the current node is being updated to the next_node
            current = current.get_next()
        # if we git here then the targeted node is not in the list
        return False
