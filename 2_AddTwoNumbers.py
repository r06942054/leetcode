# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 00:45:08 2018

@author: JayHome
"""
#solution 1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        answer = head
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l1, l2 = l1.next, l2.next
        l = l1 if l1 else l2
        while l:
            add = l.val + carry
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l = l.next
        if carry:
            head.next = ListNode(1)
        return answer.next
    
#solution 1_2
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = p = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            
            
            p.next = ListNode(val)
            p = p.next
            #p.next = p = ListNode(val)


        return head.next

    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#solution 2
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        def to_int(l):
            return l.val + 10 * to_int(l.next) if l else 0
        def to_list(val):
            l = ListNode(val % 10)
            if val > 9:
                l.next = to_list(val // 10)
            return l
        print(to_int(l1))
        print(to_int(l2))
        print(to_int(l1) + to_int(l2))
        return to_list(to_int(l1) + to_int(l2))