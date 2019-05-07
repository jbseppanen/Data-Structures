class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        prev_node = None
        while current_node is not None:
            prev_node = current_node
            if current_node.value > value:
                current_node = current_node.left
            elif current_node.value < value:
                current_node = current_node.right
            else:
                return  # Since value is already present.
        if prev_node.value > value:
            prev_node.left = BinarySearchTree(value)
        else:
            prev_node.right = BinarySearchTree(value)

    def contains(self, target):
        current_node = self
        while current_node is not None:
            if current_node.value > target:
                current_node = current_node.left
            elif current_node.value < target:
                current_node = current_node.right
            else:
                return True
        return False

    def get_max(self):
        current_node = self
        prev_node = None
        while current_node is not None:
            prev_node = current_node
            current_node = current_node.right
        return prev_node.value

    def for_each(self, cb):
        current_node = self
        if current_node.left is not None:
            current_node.left.for_each(cb)
        if current_node.right is not None:
            current_node.right.for_each(cb)
        cb(current_node.value)
