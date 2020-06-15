# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:25:04 2017

@author: elvis
"""
import numpy

#2D numpy array
np_2d=numpy.array([[1,2,3,4,5], [4,5,6,7,8]])
np_2d2=numpy.array([[2,3,4,5,6], [5,6,7,8,9]])

print(np_2d[1, 2])

print(" ")
print(" ")
print(" ")
print(" ")
print(numpy.max(np_2d[:, 1]))
print(" ")
print(" ")
print(" ")
print(" ")

np_2d2=np_2d

#print(np_2d2)

print(np_2d[1,4])
print(np_2d[-1,4])
print(" ")
print(" ")
print(" ")
print(" ")

print(max(1,2,6,4,5,5555))

print(np_2d>np_2d2)

print(np_2d)

print(np_2d.shape)   #ritorna (2L, 3L) che significa 2 rows 3 columns

print(np_2d[1][2])   #[row][col] usati come indice e mi ritorna il 6
#o anche
print(np_2d[1,2]) 
#ricorda il conteggio parte ssempre da zero e gli items sempre dello stesso tipo nei numpy arrays




print(np_2d[:, 1:3])  #prendi gli items 1 e 2 (xk il 3 è escluso) da entrambe le rows
#[[2 3][5 6]]

print(np_2d[0, :]) #da tutto il primo array cioè la prima riga
print(np_2d[1, :]) #da tutto il secondo array
print(np_2d[0])  #da tutto il primo array
print(np_2d[1])  #da tutto il secondo array
print(np_2d[:,0]) #da tutta la prima colonna etc.

