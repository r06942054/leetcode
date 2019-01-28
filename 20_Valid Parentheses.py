# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:42:17 2019

@author: JayHome
"""
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''



class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_list = []
        if s == "": return True
        if len(s) < 2 : return False
        for c in s:
            #print(c)
            if c in ['(', '[', '{']:
                p_list.append(c)
            else:
                if len(p_list)==0: return False
                if p_list[-1] + c in ['()', '{}', '[]']:
                    del p_list[-1:]
                else:
                    return False
        if p_list ==[]:
            return True
        else:
            return False