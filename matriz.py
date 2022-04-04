# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:08:18 2021

@author: Jonny
"""

import numpy as np
import  sys
N = 10

A = np.zeros((N,N))
print("A = \n",A)
np.fill_diagonal(A,2)
print("A = \n",A)
b = np.ones(N-1)
np.fill_diagonal(A[1:], b)
print("A = \n",A)
np.fill_diagonal(A[:,1:], -b)
print("A = \n", A)
