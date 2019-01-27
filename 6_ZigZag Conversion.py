# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 11:48:31 2019

@author: JayHome
"""

'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
    (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''


'''
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if length <= numRows or numRows==1:
            return s
        print(len(s))
        output=""
        
        for i in range(numRows):
            j = i
            a = 2*numRows-2 - 2 * i
            b = 0 + 2 * i
            output += s[j]
            while True:
                if j>=length :break
                j += a
                if j>=length :break
                if a != 0:
                    output += s[j]
                j += b
                if j>=length :break
                if b != 0:
                    output += s[j]
        print(output)
        return output

'''
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s: 
            L[index]+=x 
            print(L)
            if index==0: 
                step=1
            elif index==numRows-1:
                step=-1
            index+=step

        return ''.join(L)
