# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
m=5
mm=-4
def chkmatch(x,y):
    r=17
    c=17
    matrix=np.zeros((17,17))
    for i in range(1, rows):
        for j in range(1, cols):
            if (max(matrix[i][j-1],matrix[i-1][j-1],matrix[i-1][j])==matrix[i-1][j-1]):
                    matrix[i][j] = matrix[i-1][j-1]+m
            else:
                matrix[i][j]=max(matrix[i][j-1],matrix[i-1][j])-mm
    return matrix
    
def backtrack(x,y,matrix):

      