Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
    As an array = O(1)
    As a linked list = O(1)

2. What is the runtime complexity of `dequeue`?
    As an array = O(len) since under the hood each element in the array.  It would reduce to O(1), though.
    As a linked list = O(1).  It can run much faster than as an array, especially if the size of the array gets large.

3. What is the runtime complexity of `len`?
    As an array = O(1)
    As a linked list = O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?
    O(log n)
2. What is the runtime complexity of `contains`?
    O(log n)
3. What is the runtime complexity of `get_max`?
    O(log n) 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
    O(3) = O(1)
2. What is the runtime complexity of `ListNode.insert_before`?
    O(3) = O(1)
3. What is the runtime complexity of `ListNode.delete`?
    O(2) = O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    O(3) = O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    O(6) = O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    O(5) = O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    O(6) = O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    O(6) = O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    O(8) = O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(5) = O(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the
     JS `Array.splice` method. Which method generally performs better?
        Assuming JS means JavaScript and just guessing on how Array.splice acts under the hood since I 
        know next to nothing about JavaScript, I would guess that it would have a worst-case runtime of O(n) if
        the first item in the list were removed since the index of every item in the list would need to shift.
        DLL.delete's runtime is O(1) so the runtime should typically be much better than JS array.splice.
    