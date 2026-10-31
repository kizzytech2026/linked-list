
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """
        Recursively calculate the sum of all node data.
        """
        def sum_helper(node):
            if node is None:
                return 0

            return node.data + sum_helper(node.next)

        return sum_helper(self.head)

    def recursive_reverse(self):
        """
        Reverse the linked list in-place using recursion.
        """
        def reverse_helper(previous, current):
            if current is None:
                return previous

            next_node = current.next
            current.next = previous

            return reverse_helper(current, next_node)

        self.head = reverse_helper(None, self.head)

    def recursive_search(self, target):
        """
        Recursively search for a target value.
        """
        def search_helper(node):
            if node is None:
                return False

            if node.data == target:
                return True

            return search_helper(node.next)

        return search_helper(self.head)

    def display(self):
        """
        Display the contents of the linked list.
        """
        current = self.head
        values = []

        while current is not None:
            values.append(str(current.data))
            current = current.next

        print(" -> ".join(values) + " -> None")
