# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 23:52:39 2018

@author: JayHome
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxlen=len(set(s))
        #print(maxlen)
        if maxlen==0: return 0
        for i in range(maxlen,0,-1):
            #print("i=",i)
            for k in range(len(s)-i+1):
                if len(set(s[k:k+i]))==i: 
                    #print(k)
                    return i