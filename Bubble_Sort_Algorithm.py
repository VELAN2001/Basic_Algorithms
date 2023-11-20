# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 00:22:48 2023

@author: VELAN C
"""

# Python program for implementation of Bubble Sort

def bubbleSort(l):
	n = len(l)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if l[j] > l[j + 1]:
				swapped = True
				l[j], l[j + 1] = l[j + 1], l[j]
		
		if not swapped:
			return

l = [34, 64, 25, 12, 22, 11, 90]

bubbleSort(l)

print("Sorted list is:")
for i in range(len(l)):
	print("% d" % l[i], end=" ")
