"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1

    def remove_from_head(self):
        old_head_val = self.head.value
        self.head.delete()
        self.head = self.head.next
        self.length -= 1
        if self.length < 1:
            self.tail = None
        return old_head_val

    def add_to_tail(self, value):
        if self.head:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1

    def remove_from_tail(self):
        old_tail_val = self.tail.value
        self.tail.delete()
        self.tail = self.tail.prev
        self.length -= 1
        if self.length < 1:
            self.head = None
        return old_tail_val

    def move_to_front(self, node):
        node.delete()
        self.length -= 1
        self.add_to_head(node.value)

    def move_to_end(self, node):
        if node != self.tail:
            if node == self.head:
                self.head = node.next
                self.head.prev = None
            node.delete()
            self.tail.insert_after(node.value)
            self.tail = self.tail.next

    def delete(self, node):
        if node.prev is None:
            self.head = node.next
        if node.next is None:
            self.tail = node.prev
        node.delete()
        self.length -= 1
        return

    def get_max(self):
        max_val = self.head.value
        current_node = self.head
        while current_node is not None:
            if current_node.value > max_val:
                max_val = current_node.value
            current_node = current_node.next

        return max_val
