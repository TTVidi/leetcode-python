# Palindrome Linked List

# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        length = len(li)
        for i in range(length):
            if li[i] != li[length - 1 - i]:
                return False
        return True
