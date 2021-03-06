# -*- coding: utf-8 -*-
"""2_cycle3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15ib-o56pk-iqeboFAXGgbsWAMAiqW9Mz

The first step is to calculate the mean values of each column.
center the values in each column by subtracting the mean column value.
"""

import numpy as np
import numpy.linalg as nl

def getMatrix():
# reading a matrix
  R = int(input("Enter the number of rows    : "))
  C = int(input("Enter the number of columns : "))
  matrix = []
  print("Enter the elements row by row1")
  for i in range(R):
  # A for loop for row entries
    a = []
    for j in range(C):
  # A for loop for column entries
      a.append(int(input()))
    matrix.append(a)
  return(R,C,matrix)

def showMatrix():
  R,C,matrix=getMatrix()
  print("MATRIX : ")
  # For printing the matrix
  for i in range(R):
    for j in range(C):
      print(matrix[i][j],end="  ")
    print("")
  return(matrix)

matrix = showMatrix()

def calcPCA(matrix):
  A = np.array(matrix)
  #A = np.array([[1, 2], [3, 4], [5, 6]])
  #print(A)
  # M2 = np.mean(A, axis=0)
  # print(M2)
  M = np.mean(A.T, axis=1)
  print("Mean of each column : ")
  print(M)
  # center columns by subtracting column means
  C = A - M
  print("Centered matrix : ")
  print(C)
  # calculate covariance matrix of centered matrix
  V = np.cov(C.T)
  print("Covariance Matrix : ")
  print(V)
  values, vectors = nl.eig(V)
  print("Eigenvectors : ")
  print(vectors)
  print("Eigenvalues  : ",values)
  P = vectors.T.dot(C.T)
  print("Projection of original matrix : ")
  print(P.T)

calcPCA(matrix)