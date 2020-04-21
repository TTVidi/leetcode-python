# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


class MinStack:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    head = None
    min_list = None

    def __init__(self):
        return

    def push(self, x: int) -> None:
        node = self.ListNode(x)
        min_node = self.ListNode(x)
        if self.head is None:
            self.head = node
            self.min_list = node
        else:
            node.next = self.head
            self.head = node

            if self.min_list.val >= x:
                min_node.next = self.min_list
                self.min_list = min_node
            else:
                current_min = self.min_list
                pre_min = self.min_list
                while current_min is not None and current_min.val < x:
                    pre_min = current_min
                    current_min = current_min.next
                pre_min.next = min_node
                min_node.next = current_min
        return

    def pop(self) -> None:
        current_min = self.min_list
        pre_min = self.min_list
        while current_min.val != self.head.val:
            pre_min = current_min
            current_min = current_min.next
        if pre_min is current_min:
            self.min_list = pre_min.next
        else:
            pre_min.next = current_min.next

        self.head = self.head.next
        return

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.min_list.val


if __name__ == '__main__':
    l = MinStack()
    l.push(-2)
    l.push(0)
    l.push(-3)
    print(l.getMin())
    l.pop()
    l.pop()
    print(l.getMin())
