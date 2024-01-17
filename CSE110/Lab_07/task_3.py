# -*- coding: utf-8 -*-
"""task_3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

import numpy as np

def reverseArray(arr):
    l = len(arr)
    for i in range(l // 2):

        arr[i],arr[l-1-i] = arr[l-1-i], arr[i]
    return arr

arr1 = np.array([10, 12, 20, 5, 7])
arr1 = reverseArray(arr1)
print(arr1)