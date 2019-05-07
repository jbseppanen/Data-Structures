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
            if current_node.value < value:
                current_node = current_node.left
            elif current_node.value > value:
                current_node = current_node.right
            else:
                return  # Since value is already present.
        if prev_node.value < value:
            prev_node.left = BinarySearchTree(value)
        else:
            prev_node.right = BinarySearchTree(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
