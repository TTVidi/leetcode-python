#  Intersection of Two Linked Lists

# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:
#
#
# begin to intersect at node c1.
#
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while True:
            if headA:
                if headA in s:
                    return headA
                s.add(headA)
                headA = headA.next
            if headB:
                if headB in s:
                    return headB
                s.add(headB)
                headB = headB.next
            if not headA and not headB:
                break
        return None

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA and headB:
            a = headA
            b = headB
            while a != b:
                if not a:
                    a = headB
                else:
                    a = a.next
                if not b:
                    b = headA
                else:
                    b = b.next
            return a
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA and headB:
            la = 0
            lb = 0
            cu = headA
            while cu:
                la += 1
                cu = cu.next
            cu = headB
            while cu:
                lb += 1
                cu = cu.next
            dis = la - lb
            if dis > 0:
                while dis != 0:
                    headA = headA.next
                    dis -= 1
            elif dis < 0:
                while dis != 0:
                    headB = headB.next
                    dis += 1

            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
        return None
