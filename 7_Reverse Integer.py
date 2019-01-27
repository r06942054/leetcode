# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 12:07:07 2019

@author: JayHome
"""

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if len(str(x))==1: return x
        print(x > 2**31)

        if x > 2**31 or x <= -2**31: 
            return 0
        output = ""
        if x > 0:
            x = str(x)
            for i in range(len(x)-1, -1, -1):
                #print("i= ", i)
                #print(x[i])
                #print(i==len(x)-1)
                #print(x[i]=='0')
                if i==len(x)-1 and x[i]=='0': continue
                output+=x[i]
            if int(output)>2**31: 
                return 0
            else:
                return int(output)
        else:

            x = str(x)
            for i in range(len(x)-1, 0, -1):
                #print("i= ", i)
                #print(x[i])
                if i==len(x)-1 and x[i]=='0': continue
                output+=x[i]
            if -int(output) <= -2**31: 
                return 0
            else:
                return -int(output)
        #print(str(x))
        #print(output)
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        print(str(-x)[::-1])
        if x < 0:
            y = -1*int(str(-x)[::-1])
        else:
            y = int(str(x)[::-1])
        if y > 2**31 -1 or y<-2**31:
            return 0
        return y