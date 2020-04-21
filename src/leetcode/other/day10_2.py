# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
import sys


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack, self.min = [], []


    def push(self, x: int) -> None:

        self.stack.append(x)

        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x))


    def pop(self) -> None:

        self.stack.pop()
        self.min.pop()


    def top(self) -> int:

        return self.stack[-1]


    def getMin(self) -> int:

        return self.min[-1]


if __name__ == '__main__':
    l = MinStack()
    l.push(-2)
    l.push(0)
    l.push(-3)
    print(l.getMin())
    l.pop()
    l.pop()
    print(l.getMin())
