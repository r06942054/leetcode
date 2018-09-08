# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 00:28:05 2018

@author: JayHome
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = []
        while nums1!=[] and nums2!=[]:
            if nums1[-1] >= nums2[-1]:
                total.append(nums1.pop())
            else:
                total.append(nums2.pop())
        nums = nums1 if nums2==[] else nums2
        while nums!=[]:
            total.append(nums.pop())
        print(total)
        
        if len(total) % 2 == 0:
            print(total[len(total)//2-1:len(total)//2])
            medien = sum(total[len(total)//2-1:len(total)//2+1])/2
        else:
            medien = total[len(total)//2]
        return medien