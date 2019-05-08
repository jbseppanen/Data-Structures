class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) == 0:
            return None
        elif len(self.storage) == 1:
            return self.storage.pop()
        else:
            self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]
            return_val = self.storage.pop()
            self._sift_down(0)
            return return_val

    def get_max(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent
            else:
                break

    def _sift_down(self, index):
        lchild_idx = (2 * index) + 1
        rchild_idx = (2 * index) + 2
        swap_indx = -1
        if rchild_idx < len(self.storage):
            lchild = self.storage[lchild_idx]
            rchild = self.storage[rchild_idx]
            if lchild > rchild:
                swap_indx = lchild_idx
            else:
                swap_indx = rchild_idx
            if self.storage[index] < self.storage[swap_indx]:
                self.storage[index], self.storage[swap_indx] = self.storage[swap_indx], self.storage[index]
                self._sift_down(swap_indx)
        elif lchild_idx < len(self.storage):
            if self.storage[index] < self.storage[swap_indx]:
                self.storage[index], self.storage[swap_indx] = self.storage[swap_indx], self.storage[index]


# 1. Store a reference to the first heap element
# 2. Set the value of the first heap element to the value
# of the last heap element
# 3. Pop from the heap’s storage array to remove the last
# heap element
# 4. In a loop:
# 1A.Have the (new) first heap element check its two
# children using the given formulas
# B.It either of the element’s children are larger, swap
# the heap value of the parent node with the value of
# the larger child’s value via their respective indices
# 6. Continue this loop until the element is in a spot
# where neither of its children are larger than it (or it’s
# reached a spot where it has no children)
